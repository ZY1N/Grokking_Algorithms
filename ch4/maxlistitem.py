# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maxlistitem.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/18 21:26:46 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/19 20:13:07 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def maxlistitem(list):
    max = list[0]
    if (list == []):
        return max
    else :
        return maxlistitem(list[1:])


ary = [6,6,6,6,9]
x = maxlistitem(ary)
print x
