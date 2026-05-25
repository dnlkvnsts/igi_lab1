"""
Calculating the value of a function cos(x) using the power series expansion of the function.

Lab 3. Standard data types, collections, functions, and modules in Python.

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 20.03.2026
"""


import math

from  base.input import  input_in_task1, repeat_task
from  base.output import  output_in_task1 

def calculate_function_with_step_row(x, eps):
    """Calculates the function value (cos(x)) using a power series expansion.

    Args:
        x (float): The value of the argument for the function.
        eps (float): The precision for the calculation (epsilon).

    Returns:
        tuple: A tuple containing (n, func_sum), where:
            - n (int): The number of terms summed to reach the precision.
            - func_sum (float): The value of the function.
    """
    n=0
    func_sum=0
    number=1
    
    x = x % (2 * math.pi)
    while abs(number) >= eps and n < 500: 
        func_sum += number
        n += 1
        number = number * (-x**2) / ((2*n - 1) * (2*n))
    
    math_sum = math.cos(x)
        
    return n, func_sum, math_sum

def run_task1():
    """
    Release the execution of Task 1
    
    input
    calculation of cos(x)
    output.
    """
    while True: 
        x, eps =  input_in_task1()
        n, fx, math_fx = calculate_function_with_step_row(x, eps)
   
        output_in_task1(x, n, fx, math_fx, eps)
        if not repeat_task():
            break
        