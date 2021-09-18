'''
Creates a Question object/methods.
Converts question list of dictionaries into objects.
'''


class Question:

    def __init__(self, question_text, answer_text):
        self.question = question_text
        self.answer = answer_text
