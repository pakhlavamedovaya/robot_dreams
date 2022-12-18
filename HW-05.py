#------------------------------
#TASK 2
#------------------------------
symbols = input('Enter some text here: ')
for symbol in symbols:

    if symbol.isdigit():
        number = int(symbol)
        if number % 2 == 0:
            print(f'{number} is a number and it is even')
        else:
            print(f'{number} is a number and it is odd')
    elif symbol.isalnum():
        if symbol.isupper():
            print(f'{symbol} is a letter and it is upper case')
        else:
            print(f'{symbol} is a letter and it is lower case')
    else:
        print(f'{symbol} is a symbol')
#------------------------------
#TASK 2
#------------------------------
import time
while True:
    print('I love Python')
    time.sleep(4.2)
#------------------------------

