from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_answer_and_question():
    num = randint(1, 100)
    question = f'Question: {num}'
    if is_even(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    answer_and_question = (answer, question)
    return answer_and_question
