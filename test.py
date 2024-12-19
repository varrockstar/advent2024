list1 = [5, 6, 7, 8, 9]
for i in list1:
    index = list1.index(i)
    x = list1.pop(index)
    list1.insert(index, x)

