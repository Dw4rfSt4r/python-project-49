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
        i += 1
    return answers_and_questions

# code climate ругался на чрезмерную сложность.
# этот вариант проще, но лишние вычисления.


def start_calc_2():
    answers_and_questions = []
    i = 0
    while i < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        addition_result = operator.add(num_1, num_2)
        subtraction_result = operator.sub(num_1, num_2)
        multiplication_result = operator.mul(num_1, num_2)
        addition_question = f'Question: {num_1} + {num_2}'
        subtraction_question = f'Question: {num_1} - {num_2}'
        multiplication_question = f'Question: {num_1} * {num_2}'
        results_and_questions_list = [
            [addition_result, addition_question],
            [subtraction_result, subtraction_question],
            [multiplication_result, multiplication_question]]
        answers_and_questions.append(
            results_and_questions_list[randint(0, 2)])
        i += 1
    return answers_and_questions
