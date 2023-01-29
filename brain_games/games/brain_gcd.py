from math import gcd
from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def get_answer_and_question():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    answer = gcd(num_1, num_2)
    question = f'Question: {num_1} {num_2}'
    answer_and_question = (answer, question)
    return answer_and_question
