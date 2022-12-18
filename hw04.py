user_input = input("Enter something: ")
if user_input.isdigit():
        value_input = int(user_input)
        user_output = "Your input is a NUMBER"
        if (value_input % 2) == 0:
            user_input += f" {value_input} and it is Even!"
        else:
            user_output += f" {value_input} and it is Odd!"
        print(user_output)
else:
        text_length = len(user_input)
        print(f"WOW! you typed text! It has {text_length} symbols!")


