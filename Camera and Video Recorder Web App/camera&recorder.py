import cv2
from flask import Flask,render_template,session,url_for,redirect,request,flash
import webbrowser
import time
app=Flask(__name__)
app.secret_key="MYsecretKEY"
@app.route("/",methods=["GET","POST"])

def camera_selection():
    if request.method=="POST":
        camera=request.form.get("camera")
        if camera=="0":
            flash("Inbuild Camera Selected")
        else:
            flash("External Camera Selected")
        session["camera"]=camera
        return redirect(url_for('photovideo'))
    return render_template('camera.html')

@app.route("/photovideo",methods=["GET","POST"])

def photovideo():
    if request.method=="POST":
        mode=request.form.get("mode")
        if mode=="photo":
            flash("User selected camera mode")
        else:
            flash("User selected video mode")
        session["mode"]=mode
        return redirect(url_for('capture'))
    return render_template('photovideo.html')

@app.route("/capture", methods=["GET","POST"])
def capture():

    if request.method == "POST":

        start = request.form.get("start")

        if start == "1":

            camera_id = int(session.get("camera"))
            mode = session.get("mode")

            current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

            camera = cv2.VideoCapture(camera_id)

            if mode == "photo":

                while True:

                    ret, frame = camera.read()

                    if not ret:
                        flash("Couldn't access camera")
                        break

                    cv2.putText(frame,
                    "Press C to Capture | Press Q to Quit",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2)

                    cv2.imshow("Clicking Photograph", frame)

                    key = cv2.waitKey(1)

                    if key == ord('c'):
                        cv2.imwrite(f"{current_time}.jpg", frame)
                        flash("Photo Captured Successfully")
                        break

                    if key == ord('q'):
                        break

            else:

                codec = cv2.VideoWriter_fourcc(*'XVID')

                frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

                recorder = cv2.VideoWriter(
                    f"{current_time}.avi",
                    codec,
                    30,
                    (frame_width,frame_height)
                )

                while True:

                    ret, frame = camera.read()

                    if not ret:
                        flash("Couldn't access camera")
                        break

                    cv2.putText(frame,
                    "Press Q to Stop Recording",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,0,255),
                    2)

                    recorder.write(frame)

                    cv2.imshow("Recording Live", frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        flash("Recording Stopped")
                        break

                recorder.release()

            camera.release()
            cv2.destroyAllWindows()

            return redirect(url_for("camera_selection"))

    return render_template("capture.html")
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, host="127.0.0.1", port=5000, use_reloader=False)

