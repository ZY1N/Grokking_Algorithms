# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    binarysearch.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/11 18:41:02 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/11 19:14:13 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import time

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    i = 0

    while low <= high: 
        mid = (low + high)/2 
        guess = list[mid] 
#        print(guess)
        if guess == item:
            return mid
        if guess > item: 
            high = mid - 1
        else:
            low = mid + 1
        i = i + 1
    print("i is:", i)
    return None

seconds = time.time()

my_list = [ random.randint(0, 100) for i in range(1000000) ]

print binary_search(my_list, -1) # => 1 
#print binary_search(my_list, -1) # => None

print(time.time() - seconds)
