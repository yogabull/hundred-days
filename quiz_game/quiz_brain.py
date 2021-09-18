'''
Class tutorial to keep track of questions and answers.
'''


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_have_questions(self):
        # Returns True or False
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {current_question.text}. True/False: ").lower()

        self.check_answer()

    def check_answer(self):
        print(current_question.answer)
        if answer ==
