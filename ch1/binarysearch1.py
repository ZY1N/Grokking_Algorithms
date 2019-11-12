# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    binarysearch1.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/12 14:11:03 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/12 14:14:08 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def binarysearch(list, target):
    low = 0
    high = len(list)

    while low <= high:
        mid = (low + high)/2
        if (list[mid] == target):
            return mid
        elif (list[mid] < target):
            low = mid
        elif (list[mid] > target):
            high = mid
    return none

a = [0,1,2,3,4,5,6,7,8,9]

print(binarysearch(a, 9))
