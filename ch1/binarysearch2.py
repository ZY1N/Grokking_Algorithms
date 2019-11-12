# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    binarysearch2.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/11 18:47:50 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/11 19:04:30 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import random


def binarySearch(arr, l, r, x): 
  
    i = 0
    while l <= r: 
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
        i = i + 1
      
    # If we reach here, then the element 
    # was not present 
    print("i i:", i)
    return -1
  
seconds = time.time()
# Test array 
arr = [ random.randint(0, 100) for i in range(1000000) ] 
x = -1
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"

print(time.time() - seconds)
