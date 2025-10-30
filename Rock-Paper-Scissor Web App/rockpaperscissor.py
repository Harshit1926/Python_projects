from flask import Flask,render_template,request,session,url_for,redirect
import random
import webbrowser
app=Flask(__name__)
app.secret_key="IamBatman"

@app.route("/",methods=["GET","POST"])
def start_game():
    if "round_number" not in session:
        session["round_number"]=1
        session["user_score"]=0
        session["computer_score"]=0

    if request.method=="POST":
        session["computer_choice"] = random.choice(["Rock", "Paper", "Scissors"])
        computer_choice=session["computer_choice"]
        user_choice=request.form.get("user_choice")

        if computer_choice==user_choice:
            result="It's a Draw"
        elif (computer_choice=="Rock" and user_choice=="Paper" or
                computer_choice=="Paper" and user_choice=="Scissors" or
                computer_choice=="Scissors" and user_choice=="Rock"):
            result="You Won"
            session["user_score"]+=1
        else:
            result="Computer Won"
            session["computer_score"]+=1
        session["round_number"]+=1

        if session["round_number"]>3:
            if session["user_score"]>session["computer_score"]:
                final_result="Congrats! You won the Game"
            elif session["computer_score"]>session["user_score"]:
                final_result="Computer won the game"
            else:
                final_result="It's a draw"
            
            session.clear()

            return render_template("final.html",final_result=final_result,user_choice=user_choice,computer_choice=computer_choice,result=result)
        
        return render_template("result2.html",
                               user_choice=user_choice,
                               computer_choice=computer_choice,
                               result=result,
                               round_number=session["round_number"],
                               user_score=session["user_score"],
                               computer_score=session["computer_score"])
    

    return render_template("game.html",round_number=session["round_number"])

@app.route("/again",methods=["GET","POST"])
def again():
    choice=request.form.get("play_again")
    if choice=="Yes":
        session.clear()
        return redirect(url_for("start_game"))
    else:
        return(render_template("thanks.html"))

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5002")
    app.run(debug=True, host="127.0.0.1", port=5002,use_reloader=False)
    
