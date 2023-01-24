import operator
from random import randint


RULES = 'What is the result of the expression?'


def start_calc():
    answers_and_questions = []
    i = 0
    while i < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        operators = ['+', '-', '*']
        for current_operator in operators:
            current_operator = operators[randint(0, 2)]
            break
        if current_operator == '+':
            calculations = operator.add(num_1, num_2)
            question = f'Question: {num_1} + {num_2}'
        elif current_operator == '-':
            question = f'Question: {num_1} - {num_2}'
            calculations = operator.sub(num_1, num_2)
        elif current_operator == '*':
            question = f'Question: {num_1} * {num_2}'
            calculations = operator.mul(num_1, num_2)
        answer = calculations
        answers_and_questions.append([answer, question])
        i += 1
    return answers_and_questions
