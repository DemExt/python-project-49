# from brain_games import main
from random import randint


def progression():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ', name, '!', sep='')
    print('What number is missing in the progression?')
    count = 0

    while count != 3:
        x = randint(1, 10) # NOSONAR
        
        step = randint(1, 10) # NOSONAR
        progr = [x]
        length_prog = randint(5, 10) # NOSONAR
        y = randint(1, length_prog) # NOSONAR
        for i in range(length_prog):
            x += step
            progr.append(x)
        miss = progr[y]
        progr[y] = '..'
        print('Question:', *progr)
        ans = int(input())

        print('Your answer:', ans)

        if ans == miss:
            print('Correct!')
            count += 1
        if ans != miss:
            print(ans, " is wrong answer ;(. Correct answer ")
            print("was ", miss, ". Let's try again, ", name, "!", sep='')
            count = 0
            break

    if count == 3:

        print('Congratulations, ', name, '!', sep='')


if __name__ == "__progression__":
    progression()