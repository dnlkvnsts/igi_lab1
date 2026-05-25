import base.validation as val 

import random
import string


def input_in_task1():
    """
    Input values for x and the precision epsilon (eps).

    Returns:
        tuple: A tuple containing the float value of x and the positive float value of eps.
    """
    
    x=val.get_float_input("Input x:\n")

    eps=val.get_float_positive_input("\nInput eps:\n")

    return x, eps



def initialize_by_user(original_sequence):
    """
    Initializes a list of integers by asking the user for input.
    The process stops if the user enters the number 100.

    Args:
        original_sequence (iterable): A sequence .

    Returns:
        list: A list of integers provided by the user.
    """
    
    sequence = []
    
    for i in original_sequence:
        el=val.get_int_input(f"Input {i+1} integer element\n")
        sequence.append(el)
        
        if el == 100:
            break
        
    return sequence


def initialize_by_function_of_generator(original_sequence):
    """
    A generator that yields random integers between 0 and 150.
    The generation stops if the value 100 is produced.

    Args:
        original_sequence (iterable): A sequence .

    Yields:
        int: A random integer.
    """
    
    for _ in original_sequence:
        el=random.randint(0, 150)
        yield el
        
        if el == 100:
            break



def initialize_float_numbers_by_user(original_sequence):
    """
    Initializes a list of floating-point numbers by asking the user for input.

    Args:
        original_sequence (iterable): A sequence.

    Returns:
        list: A list of float numbers .
    """
    
    sequence = []
    
    for i in original_sequence:
        el=val.get_float_input(f"Input {i+1} float element\n")
        sequence.append(el)
    return sequence
    
        
        
        
def initialize_with_float_numbers_by_function_of_generator(original_sequence):
    """
    A generator that yields random float numbers between -500.0 and 500.0.

    Args:
        original_sequence (iterable): A sequence defining the number of iterations.

    Yields:
        float: A random float number.
    """
    
    for _ in original_sequence:
        el=random.uniform(-500.0, 500.0)
        yield round(el, 2)
    
    
def initialize_string_by_generator(original_sequence):
    """
    A generator that yields random characters (letters, digits, or punctuation).

    Args:
        original_sequence (iterable): A sequence .

    Yields:
        str: A single random character.
    """

    
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    
    for _ in original_sequence:
        yield random.choice(characters)
    
def repeat_task():
    """
    Asks the user if they want to repeat the task.

    Returns:
        bool: True if the user wants to repeat, False otherwise.
    """
    while True:
            choice = input("Repeat this task ?(y/n) ").lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Invalid input!!! Input y or n\n")
    