#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:29:39 2024

@author: willem
"""

import sys
import numpy

def get_user_input_x(retries):
    while retries > 0:
        x = input('Enter number x: ')
        try: 
            x = float(x)
            return x 
        except:
            print(f'{str(x)} is not numeric, please enter a numeric value for x')
            retries -= 1
    print(f'exiting after {str(retries)} retries')
    sys.exit()
    
def get_user_input_y(retries):
    while retries > 0:
        y = input('Enter number y: ')
        try: 
            y = float(y)
            return y
        except:
            print(f'{str(y)} is not numeric, please enter a numeric value for x')
            retries -= 1 
    print(f'exiting after {str(retries)} retries')
    sys.exit()

def main(): 
    retries = 3
    x = get_user_input_x(retries)
    y = get_user_input_y(retries)
    print(f'x**y = {str(x ** y)}')
    print(f'log(x) = {str(numpy.log2(x))}')
    
if __name__ == "__main__":
    main()