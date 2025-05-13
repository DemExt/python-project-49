from random import randint


def progression():
    print('What number is missing in the progression?')
    count = 0

    while count != 3:
        x = randint(1, 10)
        y = randint(1, 10)
        step = randint(1, 10)
        progr = [x]
        for i in range(9):
            x += step
            progr.append(x)
        miss = progr[y]
        progr[y] = '..'
        print('Question: ', *progr)
        ans = int(input())

        print('Your answer: ', ans)

        if ans == miss:
            print('Correct!')
            count += 1
        if ans != miss:
            print("'ans' is wrong answer ;(. Correct answer was 'n'. Let's try again, Sam!")
            count = 0
    print('Congratulations, Sam!')


if __name__ == "__progression__":
    progression()
