import prompt
import operator
from random import randint


ROUND_NUMBER = 3

user_name = prompt.string('Welcome to the Brain Games!\nMay I have your name?')


RULES = 'What is the result of the expression?'


def start_calc():
    answers_and_questions = []
    i = 0
    while i < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        operators = ['+', '-', '*']
        for current_operator in operators:
            current_operator = operators[randint(0, 2)]
            break
        if current_operator == '+':
            calculations = operator.add(num_1, num_2)
            question = f'Question: {num_1} + {num_2}'
        elif current_operator == '-':
            question = f'Question: {num_1} - {num_2}'
            calculations = operator.sub(num_1, num_2)
        elif current_operator == '*':
            question = f'Question: {num_1} * {num_2}'
            calculations = operator.mul(num_1, num_2)
        answer = calculations
        answers_and_questions.append([answer, question])
        i += 1
    print(answers_and_questions)
    return answers_and_questions


answers_and_questions = start_calc()


def welcome():
    print('Hello, ' + user_name + '!')


def print_rules(RULES):
    print(RULES)




def get_user_answer():
    user_answer = prompt.string('Your answer:')
    return user_answer


def compliment():
    print(f'Congratulations, {user_name}!')


def cycle_game():
    i = 0
    print_rules(RULES)
    while i < ROUND_NUMBER:
        question = answers_and_questions[0 + i][1]
        print(question)
        correct_answer = answers_and_questions[0 + i][0]
        user_answer = get_user_answer()
        if user_answer == str(correct_answer):
            print('Correct!')
            counter_breaker = True
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was \
{correct_answer}. Let\'s try again, {user_name}!')
            counter_breaker = False
            break
        i = i + counter_breaker
    if i == ROUND_NUMBER:
        compliment()


def main():
    user_name
    welcome()
    cycle_game()


if __name__ == '__main__':
    main()
