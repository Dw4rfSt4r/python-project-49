from random import randint


RULES = 'What number is missing in the progression?'


def start_progression():
    answers_and_questions = []
    i = 0
    while i < 3:
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
        progression_string = ''
        for element in rand_progression:
            progression_string = progression_string + ' ' + str(element)
        question = f'Question:{progression_string}'
        answers_and_questions.append([answer, question])
        i += 1
    return answers_and_questions
