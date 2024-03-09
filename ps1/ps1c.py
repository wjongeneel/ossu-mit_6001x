#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:07:10 2024

@author: willem
"""

import sys

def get_user_input(prompt: str, retry_count: int) -> float:
    """ Assumes prompt str, retry_count int, prompt is question for user input, 
            retry_count is the total amount of tries to get the appropriate 
            input (numeric)
        Returns float user_input or exits program is invalid input was given 
            {retry_count} times """
    retries = retry_count
    while retries > 0:
        user_input = input(prompt)
        try:
            user_input = float(user_input)
            return user_input
        except: 
            print(f'{str(user_input)} is not numeric, please enter a numeric value for x')
            retries -= 1
    print(f'exiting after {str(retry_count)} retries')
    sys.exit()

def calculate_interest(current_savings: float, interest_rate: float) -> float:
    """ Assumes current_savings float, interest_rate float (percentage as 
            decimal number)
        Returns interest (float) """
    return current_savings * interest_rate / 12 

def calculate_monthly_savings_increase(monthly_savings: float, semi_annual_raise: float) -> float: 
    """ Assumes monthly_savings, and semi_annual_raise (percentage as decimal 
            number) float
        Returns the increase in montly savings float """
    increase = monthly_savings * semi_annual_raise
    return increase

def calculate_total_savings(savings_rate: float, interest_rate: float, monthly_savings, semi_annual_raise: float) -> float: 
    """ Assumes savings_rate (percentage as deciimal number), interest_rate 
            (percentage as decimal number), monthy_savings, and 
            semi_annual_raise (percentage as decimal number) float
        Returns the total_savings after 36 months float """
    savings = 0
    for month in range(1,37):
        savings += calculate_interest(savings, interest_rate)
        savings += monthly_savings
        if month % 6 == 0:
            monthly_savings += calculate_monthly_savings_increase(monthly_savings, semi_annual_raise)
    return savings

def calculate_savings_rate_estimation(down_payment: float, savings: float, savings_rate: float, savings_rate_high: float, savings_rate_low: float) -> float: 
    """ Assumes down_payment, savings, savings_rate (percentage as decimal 
            number), savings_rate_high (percentage as decimal number), 
            savings_rate_low (percentage as decimal number) float
        Returns new values for savings_rate, savings_rate_high, 
            savings_rate_low (percentages as decimal number) float """
    if down_payment > savings:
        savings_rate_low = savings_rate 
        savings_rate = (savings_rate_high + savings_rate_low) / 2
    else: 
        savings_rate_high = savings_rate
        savings_rate_low = savings_rate_low 
        savings_rate = (savings_rate_high + savings_rate_low) / 2    
    return savings_rate, savings_rate_high, savings_rate_low

def main(): 
    semi_annual_raise = 0.07 # 7% semi annual raise
    r = 0.04 # 4% interest rate 
    portion_down_payment =  0.25 # 25% portion down payment 
    total_cost = 1000000 # total cost of house
    down_payment = portion_down_payment * total_cost # calculate down payment
    annual_salary = get_user_input('Enter the starting salary: ', 3) # get annual salary from user input
    monthly_salary = annual_salary / 12 # calculate montly salary 
    savings_rate_low = 0 # initialize savings_rate lower boundary
    savings_rate_high = 1 # initialize savings_rate upper boundary
    savings_rate = (savings_rate_low + savings_rate_high) / 2 # initialize savings_rate
    monthly_savings = monthly_salary * savings_rate # initialize montly_savings on base value of savings_rate
    savings = calculate_total_savings(savings_rate, r, monthly_savings, semi_annual_raise) # initialize savings on base value of savings_rate
    
    
    for i in range(0,10000):
        if abs(down_payment - savings) < 100: # exit program with exit code 0 if the savings_rate produces an acceptable estimation 
            print(f'Best savings rate: {savings_rate}')
            print(f'Steps in bisection search: {i + 1}')
            sys.exit(0) 
        # otherwise recalculate savings_rate, savingsrate upper and lower boundary, and savings
        savings_rate, savings_rate_high, savings_rate_low = calculate_savings_rate_estimation(down_payment, savings, savings_rate, savings_rate_high, savings_rate_low)
        monthly_savings = monthly_salary * savings_rate
        savings = calculate_total_savings(savings_rate, r, monthly_savings, semi_annual_raise)
    # if acceptable estimation is not found after range(0,10000) repetitions print following line
    print('It is not possible to pay the down payment in three years.')
        
if __name__ == "__main__":
    main()