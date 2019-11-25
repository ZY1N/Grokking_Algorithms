# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bsearch.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/19 20:38:02 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/19 20:51:40 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def bsearch(list, key):
    end = len(list) -1
    beginning = 0
    
    while(end >= beginning):
        mid = (end+beginning)/2
        if (list[mid] > key):
            end = mid - 1
        elif (list[mid] < key):
            beginning = mid + 1
        else:
            return mid
    return 0

list = [1,2,3,4,5,6]

x = bsearch(list, 3)
print x
