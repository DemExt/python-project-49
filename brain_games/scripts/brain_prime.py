from random import randint


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    num = ''

    while count != 3:
        x = randint(1, 100)
        print('Question: ', x)
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
        else:
            if ans == num:
                print('Correct!')
                count += 1
            elif ans != num:
                print("'no' is wrong answer ;(. " 
                "Correct answer was 'yes'. Let's try again, Bill!")
                count = 0
    print('Congratulations, Sam!')


if __name__ == "__prime__":
    prime()
