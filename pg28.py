a=int(input("enter the total numbers"))
list=[]
for i in range(a):
    c=int(input("enter the numbers"))
    if(c>100):
        c="over"
        list.append(c)
    else:
        list.append(c)
print(list)
