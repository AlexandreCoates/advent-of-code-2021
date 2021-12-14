# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:35:20 2021
Advent of code day 3
@author: alexa
"""
#load, convert str to int
input_file = open("input-day3.txt",'r').readlines()
#remove escape characters
input_file = [x.replace('\n','') for x in input_file] 

### PART 1 ###

def common_bits(input_list):
    zero_bits = [0]*len(input_list[0])
    one_bits = [0]*len(input_list[0])
    for line in input_list:#go through each line
        for bit_index in range(len(line)): #check each bit
            if line[bit_index] == '0':
                zero_bits[bit_index] +=1
            else:
                one_bits[bit_index] +=1
    return zero_bits, one_bits

zero_count, one_count = common_bits(input_file)
            
gamma = ''
epsilon = ''          
  
for bit_index in range(len(input_file[0])):
    if zero_count[bit_index] < one_count[bit_index]:
        gamma+='1'
        epsilon+='0'
    elif zero_count[bit_index] > one_count[bit_index]:
        gamma+='0'
        epsilon+='1'

##convert binary to decimal
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print('power consumption = ' + str(gamma*epsilon)) 

### PART 2 ###

#want to filter for most and least common bits in each position
#oxygen - most common bits

oxy_filter = input_file

for bit_index in range(len(input_file[0])):
    
    zero_count, one_count = common_bits(oxy_filter)
    #get most common bit for the position
    if zero_count[bit_index] > one_count[bit_index]:
        _criterion = '0'
    else:
        _criterion = '1'
    
    _passed = [] #empty list for lines that pass
    
    for line in oxy_filter:
        if line[bit_index] == _criterion:
            _passed.append(line)
            
    oxy_filter = _passed
    if len(_passed) == 1:
        break
    
#co2 - want least common bit at each point
co2_filter = input_file

for bit_index in range(len(input_file[0])):
    zero_count, one_count = common_bits(co2_filter)
    #get most common bit for the position
    if zero_count[bit_index] > one_count[bit_index]:
        _criterion = '0'
    else:
        _criterion = '1'
    
    _passed = [] #empty list for lines that pass
    
    for line in co2_filter:
        if line[bit_index] != _criterion:
            _passed.append(line)
            
    co2_filter = _passed
    if len(_passed) == 1:
        break
    
#turn to decimals and multiply
co2_filter = int(co2_filter[0],2)
oxy_filter = int(oxy_filter[0],2)

print('life support = ' + str(co2_filter*oxy_filter))