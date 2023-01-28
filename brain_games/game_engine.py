import prompt


ROUND_NUMBER = 3


def welcome():
    user_name = prompt.string('Welcome to the Brain \
Games!\nMay I have your name?')
    print('Hello, ' + user_name + '!')
    return user_name


def print_rules(rules):
    print(rules)


def get_user_answer():
    user_answer = prompt.string('Your answer:')
    return user_answer


def compliment(user_name):
    print(f'Congratulations, {user_name}!')


def play_game(return_foo, rules):
    user_name = welcome()
    i = 0
    print_rules(rules)
    while i < ROUND_NUMBER:
        answers_and_questions = return_foo()
        question = answers_and_questions[0][1]
        print(question)
        correct_answer = answers_and_questions[0][0]
        user_answer = get_user_answer()
        if user_answer == str(correct_answer):
            print('Correct!')
            i += 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was \
{correct_answer}. Let\'s try again, {user_name}!')
            break
    if i == ROUND_NUMBER:
        compliment(user_name)
