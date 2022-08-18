a=int(input())
list=[0,1]
for i in range(a-2):
    d=list[-2]+list[-1]
    list.append(d)
print(list[-1])