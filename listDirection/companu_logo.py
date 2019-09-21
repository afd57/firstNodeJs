#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter
from collections import OrderedDict


if __name__ == '__main__':
    s = input()
    number_of_char = Counter(s)
    most_common_char = number_of_char.most_common()
    
    num_set = set()
    char_list = []
    
    count = 0
    tmp = []
    num_list = []
    char_list = [] 

    for key, value in most_common_char:
        num_list.append(value)
        char_list.append(key)
    counted_num_list = Counter(num_list)
    output = []
    print(num_list)
    print(char_list)
    for i in num_list:
        if counted_num_list[i] == 1:
            output.append(f'{char_list[i]} {num_list[i]}')
        else:
            tmp_list = char_list[i : i+counted_num_list[i]]
            print(tmp_list)
            tmp_list.sort()
            output.append(f'{tmp_list[0]} {num_list[i]}')
        if len(output) == 2:
            break
    print(output)

    print(num_list)
    print(char_list)

