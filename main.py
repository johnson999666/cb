from tkinter import *
import requests
from quizbrain import QuizBrain
from quiz99 import QuizInterface
import requests
import html

response = requests.get(url='https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean')
response.raise_for_status()
question_data = response.json()
question_data = question_data['results']

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)



