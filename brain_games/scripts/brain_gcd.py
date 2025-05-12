from random import randint


def gcd():
    print('Find the greatest common divisor of given numbers.')
    count = 0

    while count != 3:
        x, y = randint(1, 100), randint(1, 100)
        print('Question: ', x, y)
        n = min(x, y)
        deli = 1
        for i in range(1, n + 1):
            if x % i == 0 and y % i == 0:
                deli = i
        ans = int(input())
    
        print('Your answer: ', ans)

        if ans == deli:
            print('Correct!')
            count += 1
        if ans != deli:
            print("'ans' is wrong answer ;(. Correct answer was 'n'. Let's try again, Sam!")
            count = 0
    print('Congratulations, Sam!')


if __name__ == "__gcd__":
    gcd()        
    


