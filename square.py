a=int(input("enter a no."))
# b=65

for y in range(1,a+1):
    
    for x in range(1,a+1):
        if ((x+y>5 and (x==a or y==a)) or y==1 or x==1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()