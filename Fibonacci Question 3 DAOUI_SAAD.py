def fibonacci(z= int(input("Entrer un nombre ?"))):
    x=1
    y=1
    print("la suite fibonacci est :")
    if z==1:
        print('0')
    elif z==2:
        print('0','1')
    else:
        print('0')
        print(x)
        print(y)
        for i in range(z-3):
            total = x + y
            y=x
            x= total
            print(total)
         
fibonacci()
