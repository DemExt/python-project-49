# from brain_games import main
from random import choice, randint


def calc():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ', name, '!', sep='')
    print('What is the result of the expression?')
    count = 0

    while count != 3:

        sym = '+-*'
        operator = choice(sym)  # NOSONAR
        x, y = randint(1, 100), randint(1, 100)  # NOSONAR
        print('Question:', x, operator, y)
        if operator == '+':
            n = x + y
        elif operator == '-':
            n = x - y
        elif operator == '*':
            n = x * y
        ans = int(input())
    
        print('Your answer: ', ans)

        if ans == n:
            print('Correct!')
            count += 1
        if ans != n:
            print("'ans' is wrong answer ;(. Correct answer ")
            print("was 'n'. Let's try again, ", name, "!", sep='')
            count = 0
            break

    if count == 3:

        print('Congratulations, ', name, '!', sep='')


if __name__ == "__calc__":
    calc()  
    