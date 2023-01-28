from random import randint


rules = 'What number is missing in the progression?'


def random_progression():
    start = randint(1, 10)
    stop = start + 200
    step = randint(1, 10)
    rand_progression = range(start, stop, step)
    return list(rand_progression[:10])


def start_progression():
    answers_and_questions = []
    rand_progression = random_progression()
    correct_element = randint(0, 9)
    answer = str(rand_progression[correct_element])
    rand_progression[correct_element] = '..'
    rand_progression = map(str, rand_progression)
    separator = " "
    progression_string = separator.join(rand_progression)
    question = f'Question: {progression_string}'
    answers_and_questions.append([answer, question])
    return answers_and_questions
