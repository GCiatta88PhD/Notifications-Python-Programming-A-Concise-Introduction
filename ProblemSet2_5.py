# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:28:43 2020

@author: Gianluca Ciattaglia
"""
"""

problem2_5()
4
5
3
1
4
3
5
1
6
3

"""
"""
Problem 2_5:
"""

#%%

import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    for r in range(0,10):
        print(random.randint(1,6))