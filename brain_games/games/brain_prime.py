from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for element in range(2, int(num ** 1 / 2) + 1):
        if num % element == 0:
            return False
    return True


def start_prime():
    answers_and_questions = []
    num = randint(2, 100)
    question = f'Question: {num}'
    if is_prime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    answers_and_questions.append([answer, question])
    return answers_and_questions
