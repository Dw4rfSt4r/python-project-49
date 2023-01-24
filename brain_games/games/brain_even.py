from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def start_even():
    answers_and_questions = []
    i = 0
    while i < 3:
        num = randint(1, 100)
        question = f'Question: {num}'
        if is_even(num) is True:
            answer = 'yes'
        else:
            answer = 'no'
        answers_and_questions.append([answer, question])
        i += 1
    return answers_and_questions
