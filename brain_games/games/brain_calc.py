import operator
from random import randint


RULES = 'What is the result of the expression?'


def start_calc():
    answers_and_questions = []
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    operators = ['+', '-', '*']
    current_operator = operators[randint(0, 2)]
    if current_operator == '+':
        answer = operator.add(num_1, num_2)
        question = f'Question: {num_1} + {num_2}'
    elif current_operator == '-':
        question = f'Question: {num_1} - {num_2}'
        answer = operator.sub(num_1, num_2)
    elif current_operator == '*':
        question = f'Question: {num_1} * {num_2}'
        answer = operator.mul(num_1, num_2)
    answers_and_questions.append([answer, question])
    return answers_and_questions
