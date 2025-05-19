# from brain_games import main
from random import randint


def gcd():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ', name, '!', sep='')
    print('Find the greatest common divisor of given numbers.')
    count = 0

    while count != 3:
        x, y = randint(1, 100), randint(1, 100) # NOSONAR
        print('Question:', x, y)
        n = min(x, y)
        deli = 1
        for i in range(1, n + 1):
            if x % i == 0 and y % i == 0:
                deli = i
        ans = int(input())
    
        print('Your answer:', ans)

        if ans == deli:
            print('Correct!')
            count += 1
        if ans != deli:
            print("'ans' is wrong answer ;(. Correct answer ")
            print("was 'n'. Let's try again, ", name, "!", sep='')
            count = 0
            break

    if count == 3:

        print('Congratulations, ', name, '!', sep='')


if __name__ == "__gcd__":
    gcd()        
    


