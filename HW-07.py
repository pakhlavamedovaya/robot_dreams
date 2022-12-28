phone_book = dict()
while True:
    command = input('add / remove / stats / list / show \n Please type 
your command from the list above: ')
    if command == 'add':
        name = input('Please enter the name: ')
        if name in phone_book:
            print(f'Sorry, can not use this name as it is already 
associated with the number {phone_book.get(name)}')
            name = input('Please enter another the name: ')
        number = input('Please enter the phone number: ')
        phone_book[name] = number
    elif command == 'remove':
        name = input('Please enter the name that you want to delete: ')
        del phone_book[name]
    elif command == 'stats':
        print(len(phone_book))
    elif command == 'list':
        for name in phone_book:
            print(name)
    elif command == 'show':
        name = input('Please enter the name: ')
        if name in phone_book:
            print(phone_book.get(name))
        else:
            print("Name not found")
    else:
        print('Invalid command. Please type one of the commands below: 
\nadd / remove / stats / list / show')



