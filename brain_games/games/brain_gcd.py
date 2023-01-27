from math import gcd
from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def start_gcd():
    answers_and_questions = []
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    answer = gcd(num_1, num_2)
    question = f'Question: {num_1} {num_2}'
    answers_and_questions.append([answer, question])
    return answers_and_questions
