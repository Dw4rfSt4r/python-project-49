from random import randint


rules = 'What number is missing in the progression?'


def random_progression():
    rand_progression_start = randint(1, 10)
    rand_progression_stop = rand_progression_start + 10
    step = randint(1, 10)
    rand_progression = []
    for element in range(rand_progression_start, rand_progression_stop):
        rand_progression.append(rand_progression_start)
        rand_progression_start = rand_progression_start + step
    return rand_progression


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
