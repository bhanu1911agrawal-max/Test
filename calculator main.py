def add_no(a,b):
    return a+b
    
def sub_no(a,b):
    if a>b:
        return a-b
    else:
        return b-a

def multi_no(a,b):
    return a*b

def divid_no(a,b):
    return a/b
while(1):   
    print()
    print()
    print("""Choose one operation:
    1. Add
    2. Subtract
    3. Multiple
    4. Divide
    5. Exit""")
    
    a=input("enter a operation :")
    
    
    print("\n\n")
    if(a=="Add"):
        A=int(input("enter a first :"))
        B=int(input("enter a second :"))
        result = add_no(A, B)
        print("Sum:", result)
    elif(a=="Subtract"):
        A=int(input("enter a first :"))
        B=int(input("enter a second :"))
        result = sub_no(A, B)
        print("Sub:", result)
    elif(a=="Multiple"):
        A=int(input("enter a first :"))
        B=int(input("enter a second :"))
        result = multi_no(A, B)
        print("multiple:", result)
    elif(a=="Divide"):
        A=int(input("enter a first :"))
        B=int(input("enter a second :"))
        result = divid_no(A, B)
        print("divid:", result)
    elif(a=="Exit"):
        break
    else:
        print("invalid command pass only one ture value in operation")
        