# from .brain_games import welcome_user

def welcome_user():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ', name, '!', sep='')


#def greet():    
    #print('Welcome to the Brain Games!')
    

def main():
    #greet()
    welcome_user()


if __name__ == "__main__":
    main()
    



