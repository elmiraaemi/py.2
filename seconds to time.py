a = int(input("saconds :"))


if 60 <= a <3600 :
    b = int( a / 60)
    c = b * 60
    d = a - c
    print(b , ":" , d)

elif a >= 3600 :
    h = int( a / 3600)
    e = h * 3600
    f = a - e
    if f < 60 :
        print(h , ":" , "00" , ":" , f )

    if f > 60 :
        g = int( f / 60)
        k = g * 60
        y = f - k
        print(h , ":" , g , ":" , y )
        
elif a < 60 :
    print("Less than a minute")
    

