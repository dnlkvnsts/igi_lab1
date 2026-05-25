"""
Realise two function: one function find amount of numbers greater than c,
second function  find mul of elements after max(abs(element))


Lab 3. Standard data types, collections, functions, and modules in Python.

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 23.03.2026
"""

from base.validation import get_int_input, get_float_input
import base.input as inp
from base.output import output_in_task5


def find_amount_of_numbers_grater_than_c(number_collection, c):
    """
    Counts how many positive numbers in a list are greater than c.

    Args:
        number_collection (list): A list of numbers.
        c (float): The  number c.

    Returns:
        int: The amount of numbers greater than c.
    """
    amount_of_numbers_greater_than_c=0
    for number in number_collection:
        if number > c and number > 0:
            amount_of_numbers_greater_than_c += 1
    return amount_of_numbers_greater_than_c


def find_mul_elements(number_collection):
    """
    Finds the number with the largest absolute value, then multiplies all numbers after it.

    Args:
        number_collection (list): A list of numbers.

    Returns:
        float or None: The multiplication result, or None if the largest number is the last one.
    """
    max_abs_el = max(number_collection, key=abs)
    max_index = number_collection.index(max_abs_el)
    
    
    if max_index == len(number_collection) - 1:
        return None 
    
    mul_elements = 1
    for i in number_collection[max_index + 1:]:
        mul_elements *= i
        
    return mul_elements
    
    

def run_task5():
    """
    Release the execution of Task 5.
    
    It asks the user for the list size and how to fill it with numbers.
    Then it asks for a number c, calculates the results using the other functions, and shows them.
    It also asks if the user wants to repeat the task.
    """
    while True:
        while True:
            number_of_elements=get_int_input("\nInput number of elements of collection\n")
            
            if number_of_elements > 0:
                break
            print("Invalid input. The sequence should have one or more elements")
        sequence=range(number_of_elements)
        
        print("\nChoose initialization method:")
        print("1. Initialize by user (return)")
        print("2. Initialize by generator function (yield)")
        print("0. Go back to change amount of elements")
        
        number_collection=[]
        while True:
            choice=input("make a choice (0,1 or 2)\n")
            
            if choice == "1":
                number_collection=inp.initialize_float_numbers_by_user(sequence)
                break
            elif choice == "2":
                number_collection=list(inp.initialize_with_float_numbers_by_function_of_generator(sequence))   
                break
            elif choice == "0":   
                break
            else:
                print("Invalid input.Choose right option\n")
                
        if choice == "0":
            continue
                
        print(f"Collection {number_collection}")
                
        number_c=get_float_input("Input a float number C to find amount of numbers greater than C \n")
        
        print(f"Number c = {number_c}")
        
        amount_of_numbers_grater_than_c=find_amount_of_numbers_grater_than_c(number_collection, number_c)
                
        mul_elements=find_mul_elements(number_collection)
        
        output_in_task5(number_collection, amount_of_numbers_grater_than_c, mul_elements)
        if not inp.repeat_task():
            break
        
        
        