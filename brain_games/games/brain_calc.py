from random import randint
from random import choice
import operator


rules = 'What is the result of the expression?'


def start_calc():
    answers_and_questions = []
    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    rand_operator_list = [
        [operator.sub, '-'], [operator.add, '+'], [operator.mul, '*']]
    operator_foo_and_str = choice(rand_operator_list)
    answer = operator_foo_and_str[0](num_1, num_2)
    question = f'Question: {num_1} {operator_foo_and_str[1]} {num_2}'
    answers_and_questions.append([answer, question])
    return answers_and_questions
