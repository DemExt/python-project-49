# from brain_games import main
from random import randint


def prime():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ', name, '!', sep='')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    num = ''

    while count != 3:
        x = randint(1, 100) # NOSONAR
        print('Question:', x)
        ans = input()
        print('Your answer:', ans)
        n = x + 1
        for i in range(2, n // 2):
            if x % i == 0:
                num = 'no'
                break
            else:
                num = 'yes'
        if ans != 'yes' and ans != 'no':
            print('you must answer "yes"/"no"')
            count = 0
            break
        else:
            if ans == num:
                print('Correct!')
                count += 1
            elif ans != num:
                print("'no' is wrong answer ;(. Correct answer ")
                print("was 'yes'. Let's try again, ", name, "!", sep='')
                count = 0
                break

    if count == 3:

        print('Congratulations, ', name, '!', sep='')


if __name__ == "__prime__":
    prime()