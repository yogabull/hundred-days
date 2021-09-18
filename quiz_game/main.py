from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

# solution from tutorial
for item in question_data:
    q_text = item['text']
    q_answer = item['answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()
