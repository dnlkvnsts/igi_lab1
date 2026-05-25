"""
The loop counts the number of lowercase characters and the number of digits

Lab 3. Standard data types, collections, functions, and modules in Python.

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 20.03.2026
"""

from base.output import output_in_task3
from base.input import repeat_task, initialize_string_by_generator
from base.validation import get_int_input, get_string


def calculate_numbers_of_lowerletters_and_digits(text):
    """Calculate the number of lowercase letters and  digits in a string.

    Args:
        text (str): The input text string.

    Returns:
        tuple: A tuple containing two integers:
            - amount_of_digits (int): Total count of digits.
            - amount_of_letters (int): Total count of lowercase characters.
    """
    amount_of_digits=0
    amount_of_letters=0
    
    for symbol in text:
        if symbol.islower():
            amount_of_letters += 1
        elif symbol.isdigit():
            amount_of_digits += 1
            
    return amount_of_digits, amount_of_letters


def run_task3():
    """
    Release the execution of Task 3.
    
    It asks the user how to create a string (type it manually or generate it).
    Then it counts the lowercase letters and digits in the string and shows the result.
    It also asks if the user wants to repeat the task.
    """
    while True:
        
        
        print("\nChoose initialization method:")
        print("1. Initialize by user ")
        print("2. Initialize by generator function ")
        
        text = ""
        while True:
            choice = input("Make a choice ( 1 or 2)\n")
            
            if choice == "1":
                text = get_string("Please, input your string:\n")
                break
            elif choice == "2":
                while True:
                    length_of_string = get_int_input("\nInput the length of the string for initialize by generator function\n")
            
                    if length_of_string > 0:
                        break
                    print("Invalid input. The string should have at least 1 character.")
            
                sequence = range(length_of_string)
                text = "".join(initialize_string_by_generator(sequence))
                print(f"Generated string: {text}")
                break
            else:
                print("Invalid input. Choose right option\n")
                

        
        amount_of_digits, amount_of_letters = calculate_numbers_of_lowerletters_and_digits(text)
        
        
        output_in_task3(text, amount_of_digits, amount_of_letters)
        
        if not repeat_task():
            break
    