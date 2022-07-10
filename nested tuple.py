input_string = input('Enter elements: ')
list1 = input_string.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
tup= [[0]*2]*len(list1)
for i in range(len(list1)):
    tup[i][0]=list1[i]
    tup[i][1]=list1[i]**3
    tup[i]=tuple(tup[i])
print(tuple(tup))