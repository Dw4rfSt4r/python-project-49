import operator
from random import randint


rules = 'What is the result of the expression?'


def rand_operator():
    operators = ['+', '-', '*']
    random_operator = operators[randint(0, 2)]
    return random_operator


def start_calc():
    answers_and_questions = []
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    random_operator = rand_operator()
    if random_operator == '+':
        answer = operator.add(num_1, num_2)
    elif random_operator == '-':
        answer = operator.sub(num_1, num_2)
    elif random_operator == '*':
        answer = operator.mul(num_1, num_2)
    question = f'Question: {num_1} {random_operator} {num_2}'
    answers_and_questions.append([answer, question])
    return answers_and_questions
