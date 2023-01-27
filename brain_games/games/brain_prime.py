from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for element in range(2, int(num ** 1 / 2)):
        if num % element == 0:
            return False


def start_prime():
    answers_and_questions = []
    num = randint(2, 3391)
    question = f'Question: {num}'
    answer = 'yes'
    if not is_prime(num):
        answer = 'no'
    answers_and_questions.append([answer, question])
    return answers_and_questions
