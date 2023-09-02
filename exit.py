b = 0
print("if you wont to exit, type exit   else type yor namber")
while True:
    a = input("your namber : ")
    if a=='exit':
        break
    else :
        b = int(a) + b
print(b)
