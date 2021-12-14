# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:03:36 2021
Advent of Code Day 1
@author: alexa
"""

### PART 1 ### 

#load, convert str to int
input_file = open("input-day1.txt",'r').readlines()
input_file = [int(x) for x in input_file]
#set count to 0 and define initial read
increase_count = 0
previous_measure = input_file[0]
#compare
for measure in input_file:
    if measure > previous_measure:
           increase_count +=1
    previous_measure = measure
    
print(increase_count)

### PART 2 ###

window_increase_count = 0
previous_window = sum(input_file[0:3])

for index in range(len(input_file)):
    window = sum(input_file[index:index+3])
    if window > previous_window:
           window_increase_count +=1
    previous_window = window
    
print(window_increase_count)