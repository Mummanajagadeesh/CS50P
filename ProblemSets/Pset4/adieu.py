list1=[]
str1=''
try:
    while(True):
        test=str(input("Name:"))
        list1.append(test)
except EOFError:
    print("Adieu, adieu, to ",end="")
    if len(list1)==1:
        print(list1[0])
    elif len(list1)==2:
        print(list1[0]+" and "+list1[1])
    elif len(list1)>2:
        n=len(list1)
        for i in range(n-1):
            str1+=list1[i]+", "
        print(str1+"and "+list1[n-1])
