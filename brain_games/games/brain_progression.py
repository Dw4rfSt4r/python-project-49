from random import randint


RULES = 'What number is missing in the progression?'


def start_progression():
    answers_and_questions = []
    rand_progression_start = randint(1, 10)
    rand_progression_stop = rand_progression_start + 10
    step = randint(1, 10)
    rand_progression = []
    for element in range(rand_progression_start, rand_progression_stop):
        rand_progression.append(rand_progression_start)
        rand_progression_start = rand_progression_start + step
    correct_element = randint(0, 9)
    answer = str(rand_progression[correct_element])
    rand_progression[correct_element] = '..'
    progression_list = []
    for element in rand_progression:
        element = str(element)
        progression_list.append(element)
    separator = " "
    progression_string = separator.join(progression_list)
    question = f'Question: {progression_string}'
    answers_and_questions.append([answer, question])
    return answers_and_questions
