def get_non_empty_string(prompt: str):
    '''
    This function takes and validates a
    non empty string from the user
    :param prompt: str msg
    :return: non empty string value
    '''
    while True:
        user_input = input(prompt)
        if len(user_input) > 0:
            break
        else:
            print("Please enter a non empty value")

    return user_input


def get_1_to_20_length_word(prompt: str):
    while True:
        user_input = input(prompt)
        if 0 < len(user_input) < 20:
            break
        else:
            print("Your name is incorrect, either empty or too long, try again")

    return user_input

def get_positive_integer(prompt):
    '''
    This function takes and validates a
    positive number
    :param prompt: int number
    :return: a positive number
    '''
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                break
            else:
                print("Please enter a positive value only: ")
        except ValueError:
            print("Please enter a numeric value only")
    return user_input


def numeric_and_6_dig(prompt):
    while True:
        try:
            user_input = input("Enter a number: ")
            if user_input.isnumeric() and len(user_input) == 6:
                break
            else:
                print("Please enter a number that is 6 digits long")
        except ValueError:
            print("Please enter a numeric value only")

    return user_input


def get_number_in_range(val1: int, val2: int):
    '''
    This function takes and validates a number between range val1-val2
    :param val1: int lower limit
    :param val2: int higher limit
    :return: User_input an integer between val1 and val2
    '''

    while True:
            user_input = int(input("Enter a number: "))
            if val1 <= user_input <= val2:
                break
            else:
                print("Please enter a number in range and that would make sense: ")

    return user_input

if __name__ == "__main__":
    test_number = get_positive_integer("Enter a number: ")
    test_string = get_non_empty_string("Enter a string: ")
    num_in_range = get_number_in_range(1, 100)
    test_name = get_1_to_20_length_word("Enter a name: ")
    test_6_number = numeric_and_6_dig("Enter a 6 digit number")
