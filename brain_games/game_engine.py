import prompt


ROUND_NUMBER = 3


def get_user_name():
    user_name = prompt.string('Welcome to the Brain \
Games!\nMay I have your name?')
    return (user_name)


user_name = get_user_name()


def welcome():
    print('Hello, ' + user_name + '!')


def print_rules(RULES):
    print(RULES)


def get_user_answer():
    user_answer = prompt.string('Your answer:')
    return user_answer


def compliment():
    print(f'Congratulations, {user_name}!')


def cycle_game(answers_and_questions, RULES):
    question = answers_and_questions[0][1]
    print(question)
    correct_answer = answers_and_questions[0][0]
    user_answer = get_user_answer()
    if user_answer == str(correct_answer):
        print('Correct!')
        return True
    else:
        print(f'{user_answer} is wrong answer ;(. Correct answer was \
{correct_answer}. Let\'s try again, {user_name}!')
        return False
