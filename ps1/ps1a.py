#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 8 11:00:00 2024

@author: willem
"""
import sys

def get_user_input(prompt: str, retry_count: int) -> float:
    """ Assumes prompt str, retry_count int, prompt is question for user input, 
            retry_count is the total amount of tries to get the appropriate 
            input (numeric)
        Returns float user_input or exits program is invalid input was given 
            {retry_count} times"""
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

def main(): 
    r = 0.04 # 4% interest rate 
    portion_down_payment =  0.25 # 25% portion down payment 
    current_savings = 0 # initialize current_savings 0
    annual_salary = get_user_input('Enter your annual salary: ', 3)
    portion_saved = get_user_input('Enter the percent of your salary to save, as a decimal: (example: .10 for 10%): ', 3)
    total_cost = get_user_input('Enter the cost of your dream home: ', 3)
    dest_amount = total_cost * portion_down_payment # calculate needed amount for downpayment 
    months = 0 # initialize months 0
    monthly_savings = annual_salary / 12 * portion_saved 
    
    while current_savings < dest_amount:
        current_savings += calculate_interest(current_savings, r)
        current_savings += monthly_savings
        months += 1
    
    print(f'Number of months: {months}')
    
    
if __name__ == "__main__":
    main()