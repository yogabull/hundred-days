'''
Class tutorial to keep track of questions and answers.
'''


class QuizBrain:

    def __init__(self, question_bank):
        self.question_bank = question_bank  # list of question objects
        self.q_number = 0
        self.score = 0

    def have_more_questions(self):
        return self.q_number < len(self.question_bank)

    def next_question(self):
        current_question = self.question_bank[self.q_number].question
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question}. True/False: ")
