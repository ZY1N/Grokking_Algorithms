def max(list):
    if len(list) == 1:
        return list[0]
    else:
        if(list[0] > list[1]):
            list.pop(1)
        else:
            list.pop(0)
        return max(list)

ary = [1,2,3,4]
x = max(ary)
print x
