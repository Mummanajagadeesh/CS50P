list1=[]
list2=[]
while True:
	try:
		item=input("").upper()
		list1.append(item)
		list1.sort()
	except EOFError:
		for i in range(len(list1)):
			if list1[i] not in list2:
				list2.append(list1[i])
				print(str(list1.count(list1[i]))+" "+list1[i])
		break
