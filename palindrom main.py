original = input("enter a word :")
i=len(original)
# print(i)
rev=""

while(i>0):
    rev +=original[i-1]
    
    i-=1
if original==rev:
    print ("its a palindrome")
else:
    print("not a palindrome")