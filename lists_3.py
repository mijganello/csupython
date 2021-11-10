list_1 = [1, 5, 9]
list_2 = [2, 5, 13]
new_list = []
   
   
   
temp = list_1 + list_2
while temp:
    new_list.append(temp.pop(temp.index(min(temp))))
print(new_list)
