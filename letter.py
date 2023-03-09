name="meeraa"
counter={}
for i in name:
    if i in counter:
        counter[i]=counter[i]+1
    else:
        counter[i]=1
print(counter)

maxCount=0
mostOccurring=""
for i in counter:
    if counter[i]>maxCount:
        maxCount=counter[i]
        mostOccurring=i
print(mostOccurring)
list=[]
for i in counter:
    if counter[i]==maxCount:
        list.append(i)
print(list)
        
    
        
