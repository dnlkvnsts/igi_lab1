"""
The loop counts the amount of numbers less than 10 and ends when it reaches 100

Lab 3. Standard data types, collections, functions, and modules in Python.

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 20.03.2026
"""

import base.validation as val
from base.input import initialize_by_user, initialize_by_function_of_generator, repeat_task
from base.output import output_in_task2


def find_amount_of_numbers_in_sequence(size_of_collection):
    """Counts integers less than 10 in a sequence until the number 100 is encountered.
    
    Args:
        number_collection (list of int): A sequence of integer numbers. 

    Returns:
        amount_of_numbers(int): The total count of numbers in the sequence that are less than 10. 
    """
    amount_of_numbers=0
    for number in size_of_collection:
        
        if number == 100:
            break
        
        
        if number < 10:
            amount_of_numbers += 1
    return amount_of_numbers



def run_task2():
    """
    Release the execution of Task 2
    
    It asks the user for the list size and how to fill it (by user or by generator).
    Then it counts numbers smaller than 10 and shows the result.
    It also asks if the user wants to repeat the task.
    """
    while True:
        while True:
            number_of_elements=val.get_int_input("\nInput number of elements of collection\n")
            
            if number_of_elements > 0:
                break
            print("Invalid input. THe sequence should have one or more elements")
        
        sequence=range(number_of_elements)
        
        print("\nChoose initialization method:")
        print("1. Initialize by user (return)")
        print("2. Initialize by generator function (yield)")
        print("0. Go back to change amount of elements")
        
        number_collection=[]
        while True:
            choice=input("make a choice (1 or 2)\n")
            
            if choice == "1":
                number_collection=initialize_by_user(sequence)
                break
            elif choice == "2":
                number_collection=list(initialize_by_function_of_generator(sequence))   
                break
            elif choice == "0":   
                break
            else:
                print("Invalid input.Choose right option\n")
        
        if choice == "0":
            continue
    
        amount_of_numbers=find_amount_of_numbers_in_sequence(number_collection)
    
        output_in_task2(amount_of_numbers, number_collection)
    
        if not repeat_task():
            break
    
    
        