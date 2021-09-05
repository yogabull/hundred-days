'''
Returns question object.

Parameters:
arg1 (str): Question
arg2 (str): answer of "True" or "False"

Returns:
Object with a question and matching answer.
'''


class Question:

    def __init__(self, text_q, answer_q):
        '''Takes '''
        self.text = text_q
        self.answer = answer_q
