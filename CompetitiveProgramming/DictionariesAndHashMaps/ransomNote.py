#!/bin/python3

#https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    
    magazine_dict = defaultdict(int)
    for word in magazine:
        magazine_dict[word]+=1
    for word in note: 
        if magazine_dict[word]==0 : 
            print('No') 
            return
        magazine_dict[word]-=1
    print('Yes')       
        
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
