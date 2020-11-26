from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import random
from random import choice, sample
from surveys import Question, Survey, satisfaction_survey
app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

answer_list = []

@app.route('/home')
def home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    survey = satisfaction_survey
    return render_template('home.html', title=title, instructions=instructions, survey=survey)

@app.route('/questions', methods=["GET"])
def questions():
    unit = len(answer_list)
    if len(answer_list) == len(satisfaction_survey.questions):
        return f"<html>THANK YOU!</html>"
    return render_template('questions.html', answers=answer_list, question=satisfaction_survey.questions[unit].question, choices=satisfaction_survey.questions[unit].choices)

@app.route('/questions/answers', methods=["POST"])
def answers():
    if len(request.form) == 0:
        return redirect('/questions')
    else:
        answer_list.append(request.form)
        return redirect('/questions')