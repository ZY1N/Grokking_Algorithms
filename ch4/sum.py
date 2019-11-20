# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sum.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/13 20:34:30 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/13 20:55:42 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sum(list):
    if(len(list) == 1):
        return list[0]
    elif(len(list) == 0):
        return 0
    else:
        tmp = list.pop(0)
        return (tmp + sum(list))

ary = [] 
#= [2,4,6]

print(sum(ary))
