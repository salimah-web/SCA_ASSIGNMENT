# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 05:09:41 2020

@author: salima omari
"""


# This is to determine the area of a room during a building construction.
# Given a length(l) and breadth (b); we can run these codes to determine the area.


def room_area():
    l=input('What is the length?\n>>>')
    b=input('what is the breadth?\n>>>')
    if not l.isdigit() or not b.isdigit():
        print('wrong input,it should be in digits.')
    else:
        print(f'Area is {int(l)*int(b)}')
room_area()