# from .brain_games import welcome_user

def welcome_user():
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ', name, '!', sep='')


def greet():    
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    greet()
    

if __name__ == "__main__":
    main()
    



