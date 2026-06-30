firstdic={"a": 1, "b": 2, "c": 3}
secdic={}
for x in firstdic:
    secdic[firstdic[x]]=x
    
print(secdic)