import prompt


ROUND_NUMBER = 3


def welcome():
    user_name = prompt.string('Welcome to the Brain \
Games!\nMay I have your name?')
    print('Hello, ' + user_name + '!')
    return user_name


def get_user_answer():
    user_answer = prompt.string('Your answer:')
    return user_answer


def play(take_answer_and_question, rules):
    user_name = welcome()
    i = 0
    print(rules)
    while i < ROUND_NUMBER:
        answer_and_question = take_answer_and_question()
        question = answer_and_question[1]
        print(question)
        correct_answer = answer_and_question[0]
        user_answer = get_user_answer()
        if user_answer == str(correct_answer):
            print('Correct!')
            i += 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was \
{correct_answer}. Let\'s try again, {user_name}!')
            break
    if i == ROUND_NUMBER:
        print(f'Congratulations, {user_name}!')
