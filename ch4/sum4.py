# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sum4.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/18 21:20:32 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/18 21:23:15 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sum(list):
    if (list == []) :
        return 0
    else :
        return(list[0] + sum(list[1:]))

ary = [1,2,3]

x = sum(ary)
print(x)
