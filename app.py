from flask import Flask, render_template, request, redirect
import backEnd

app=Flask(__name__)

@app.route('/')
def home():
    """
    The main page of the website. Enter questions here.
    """
    return render_template('home.html',first=True)

@app.route('/question')
def question():
    question=request.args.get('question')
    answer=backEnd.find_answer(question)
    return render_template('home.html',first=False,question=question,answer=answer)

if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
