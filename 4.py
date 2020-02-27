list=[]
new_list=[]

for i in range(0,12):
	n = int(input())
	list.append(n)

print(list)

for k in list:
	if k not in new_list:
		new_list.append(k)

print(new_list)		