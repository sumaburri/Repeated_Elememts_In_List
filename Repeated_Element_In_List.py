li=eval(input('Enter a List : '))
new_list=[]
new_list1=[]

for num in li:
    if num not in new_list:
        new_list.append(num)
for num1 in new_list:
    if li.count(num1)>1:
        new_list1.append(num1)
print(new_list1)
        
