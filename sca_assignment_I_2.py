# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 05:09:41 2020

@author: salima omari
"""


# This is to determine the area of a room during a building construction.
# Given a length(l) and breadth (b); we can run these codes to determine the area.


def room_area():
    try:
        l=float(input('What is the length?\n>>>'))
        b=float(input('what is the breadth?\n>>>'))
        print(f'Area is {l*b}')
    except ValueError:
        print('wrong input,it should be a number.')
room_area()