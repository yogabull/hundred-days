from question_model import Question
from data import question_data
from pprint import pprint
import random

question_bank = []
for i, q in enumerate(question_data):
    new_question = Question(q['text'], q['answer'])
    newer_question = i, new_question
    question_bank.append(newer_question)

q_number = random.choice(question_bank)
print(q_number)

q_print = (question_bank[q_number][1].text)
q_answer = (question_bank[q_number][1].answer)

print(q_print)
print(q_answer)
