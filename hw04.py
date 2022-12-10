user_input = input("Enter something: ")
while True:
    try:
        value_input = int(user_input)
        user_output = "Your input is a NUMBER"
        if (value_input % 2) == 0:
            user_input += f" {value_input} and it is Even!"
        else:
            user_output += f" {value_input} and it is Odd!"
        print(user_output)
        break
    except ValueError:
        text_length = len(user_input)
        print(f"WOW! you typed text! It has {text_length} symbols!")
        break

