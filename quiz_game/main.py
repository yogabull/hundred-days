from question_model import Question
from data import question_data
from pprint import pprint
import random

question_bank = []
for q in question_data:
    new_question = Question(q['text'], q['answer'])
    question_bank.append(new_question)

q_option = random.choice(question_bank)

q_print = (q_option.text)
q_answer = (q_option.answer)

print(q_print)
print(q_answer)
