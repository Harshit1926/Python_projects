import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from embedder import build_vector_store
from RAG import ask
import webbrowser

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "data", "uploads")
VECTOR_STORE_PATH = os.path.join(BASE_DIR, "data", "vector_store")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(VECTOR_STORE_PATH, exist_ok=True)

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "txt"}

MODEL_NAME = "all-MiniLM-L6-v2"

print("Loading embedding model...")
model = SentenceTransformer(MODEL_NAME)
index, chunks = None, None


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    global index, chunks

    if "file" not in request.files:
        return redirect(url_for("home"))

    file = request.files["file"]
    if file.filename == "" or not allowed_file(file.filename):
        return redirect(url_for("home"))

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    print(f"Processing {filename}...")
    index, chunks = build_vector_store(file_path, model, store_path=VECTOR_STORE_PATH)

    session["filename"] = filename
    return redirect(url_for("chat"))


@app.route("/chat", methods=["GET"])
def chat():
    filename = session.get("filename", None)
    if not filename:
        return redirect(url_for("home"))
    return render_template("chat.html", filename=filename)


@app.route("/ask", methods=["POST"])
def ask_question():
    global index, chunks

    query = request.form.get("query", "").strip()
    if not query or index is None:
        return redirect(url_for("chat"))

    answer, retrieved = ask(query, index, chunks, model)

    return render_template(
        "result.html",
        query=query,
        answer=answer,
        sources=retrieved,
        filename=session.get("filename")
    )


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)