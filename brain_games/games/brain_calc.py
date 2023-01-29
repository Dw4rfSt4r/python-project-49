from random import randint
from random import choice
import operator


RULES = 'What is the result of the expression?'


def get_answer_and_question():
    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    operators_list = [
        [operator.sub, '-'], [operator.add, '+'], [operator.mul, '*']]
    operation, symbol = choice(operators_list)
    answer = operation(num_1, num_2)
    question = f'Question: {num_1} {symbol} {num_2}'
    answer_and_question = (answer, question)
    return answer_and_question
