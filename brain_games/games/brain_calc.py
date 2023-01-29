from random import randint
from random import choice
import operator


rules = 'What is the result of the expression?'


def start_calc():
    answers_and_questions = []
    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    rand_calculations = [
        [operator.sub, '-'], [operator.add, '+'], [operator.mul, '*']]
    random_operator = choice(rand_calculations)
    answer = random_operator[0](num_1, num_2)
    question = f'Question: {num_1} {random_operator[1]} {num_2}'
    answers_and_questions.append([answer, question])
    return answers_and_questions
