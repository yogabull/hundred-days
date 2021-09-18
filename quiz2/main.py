'''
True/False Game
Use Question module
Use quiz_brain question bank.
'''

from pprint import pprint
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# Takes question list and converts each to objects.
for item in question_data:
    new_question = Question(item['text'], item['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.have_more_questions:
    quiz.next_question()
