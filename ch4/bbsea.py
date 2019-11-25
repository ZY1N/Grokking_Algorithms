# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    binarysearmine.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/11 19:54:57 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/19 20:46:35 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def bsearch(list, thing):
    high = len(list) - 1
    low = 0

    while(low <= high):
        mid = (low + high) /2
        #print(high)
        if(list[mid] == thing):
            return mid
        elif(list[mid] < thing):
            low = mid
        elif(list[mid] > thing):
            high = mid
    return 0

a = [1,2,3,4,5,6,7,8,9]

print(bsearch(a, 7))
