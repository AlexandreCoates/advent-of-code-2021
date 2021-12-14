# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:03:09 2021
Day 2 advent of code
@author: alexa
"""
#load, convert str to int
input_file = open("input-day2.txt",'r').readlines()
### PART 1 ###

#initial values
x_position = 0
depth = 0

#function for parsing commands
def parse_directions(command):
    direction, value = command.split(" ")
    diff_x = 0
    diff_depth = 0
    value = int(value)
    
    if direction == "forward":
        diff_x = value
    if direction == "down":
        diff_depth = value
    if direction == "up":
        diff_depth = -value
    return diff_x, diff_depth

#consider every instruction and unpack 
for line in input_file:
    diff =  parse_directions(line)
    x_position += diff[0]
    depth += diff[1]
    
print(x_position*depth)
        
### PART 2 ###
#initial values
x_position = 0
depth = 0
aim = 0
#update commands and take in aim as argument
def parse_directions_and_aim(command, aim):
    direction, value = command.split(" ")
    diff_x = 0
    diff_depth = 0
    diff_aim = 0
    value = int(value)
    
    if direction == "forward":
        diff_x = value
        diff_depth = value*aim
    if direction == "down":
        diff_aim = value
    if direction == "up":
        diff_aim = -value
    return diff_x, diff_depth, diff_aim

for line in input_file:
    diff =  parse_directions_and_aim(line, aim)
    x_position += diff[0]
    depth += diff[1]
    aim += diff[2]

print(x_position * depth)