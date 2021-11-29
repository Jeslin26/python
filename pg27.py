list1=[12,45,85,22,-52,-61,41]
list2=[1,5,8,4,85]
print(len(list1))
print(len(list2))
if len(list1)==len(list2):
    print("length is same")
else:
    print("length is different")
sum1=0
for i in list1:
    sum1=sum1+i
print("sum of the list 1 is",sum1)
sum2=0
for i in list2:
    sum2=sum2+i
print("sum of list 2 is",sum2)
if(sum1==sum2):
    print("sum is same")
else:
    print("sum is different")
    
