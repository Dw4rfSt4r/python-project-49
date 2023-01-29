from random import randint


RULES = 'What number is missing in the progression?'


def get_random_progression():
    start = randint(1, 10)
    stop = start + 200
    step = randint(1, 10)
    random_progression = range(start, stop, step)
    return list(random_progression[:10])


def get_answer_and_question():
    random_progression = get_random_progression()
    missing_element = randint(0, 9)
    answer = str(random_progression[missing_element])
    random_progression[missing_element] = '..'
    random_progression = map(str, random_progression)
    separator = " "
    progression_string = separator.join(random_progression)
    question = f'Question: {progression_string}'
    answer_and_question = (answer, question)
    return answer_and_question
