camel=str(input("camelCase:"))
snake=""
for i in camel:
	if i.isupper()==True:
		snake+="_"+i.lower()
	else:
		snake+=i
print("snake_case:",snake)out
