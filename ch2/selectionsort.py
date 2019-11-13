# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    selectionsort.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/12 21:08:42 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/12 21:08:43 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def findSmallest(arr):
    index = 0
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index

def selectionSort(arr):
    newary = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newary.append(arr.pop(smallest))        
        #newary.append(arr[smallest])
        #arr.pop(smallest)
    return newary

arr = [1,0, 6, 1, 9, 8, 7]

newary = selectionSort(arr)

print newary

