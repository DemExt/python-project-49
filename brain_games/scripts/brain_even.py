# from brain_games import main
from random import randint


def even():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ', name, '!', sep='')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    count = 0
    while count != 3:
        
        n = randint(1, 100)  # NOSONAR
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
                print("'yes' is wrong answer ;(. Correct answer ", end='') 
                print("was 'no'. Let's try again, ", name, "!", sep='')
                count = 0
                break
            elif ans == 'no' and n % 2 == 1:
                print('Correct!')
                count += 1
            elif ans == 'no' and n % 2 == 0:
                print("'no' is wrong answer ;(. Correct answer ", end='') 
                print("was 'yes'. Let's try again, ", name, "!", sep='')
                count = 0
                break
    if count == 3:
      
        print('Congratulations, ', name, '!', sep='')
        

if __name__ == "__even__":
    even()