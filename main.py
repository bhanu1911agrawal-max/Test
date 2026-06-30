a=int(input("enter a no. :"))
for x in range (a):
    for y in range (a):
        if x==y or x==0 or y==a-1 :
            print( 0,end=" ")
        else:
            if x<=y:
                print(" ", end=" ")
            else:
                print("", end=" ")
    print()
for x in range (a-1,0,-1):
    for y in range (1,a+1,1):
        if x==y or x==1 or y==a:
            print( 0,end=" ")
        else:
            if x<=y:
                print(" ", end=" ")
            else:
                print("", end=" ")
    print()