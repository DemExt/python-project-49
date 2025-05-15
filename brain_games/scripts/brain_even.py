from random import randint


def even():

    #print('Answer "yes" if the number is even, otherwise answer "no".')
    
    count = 0
    while count != 3:

        print('Answer "yes" if the number is even, otherwise answer "no".11')
        n = randint(1, 100)
        print('Question:', n)
        ans = input()
        print('Your answer:', ans)

        if ans != 'yes' and ans != 'no':
            print('you must answer "yes"/"no"')
            count = 0
        else:
            if ans == 'yes' and n % 2 == 0:
                print('Correct!')
                count += 1
            elif ans == 'yes' and n % 2 == 1:
                print("'yes' is wrong answer ;(. " 
                "Correct answer was 'no'. Let's try again, Bill!")
                count = 0
            elif ans == 'no' and n % 2 == 1:
                print('Correct!')
                count += 1
            elif ans == 'no' and n % 2 == 0:
                print("'no' is wrong answer ;(. " 
                "Correct answer was 'yes'. Let's try again, Bill!")
                count = 0
    print('Congratulations, Sam!')
        

if __name__ == "__even__":
    even()
even()