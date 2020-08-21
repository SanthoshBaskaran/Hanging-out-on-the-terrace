max_people=list(map(int,input().split()))
result=0
count=0
for i in range(max_people[1]):
    a=input().split()
    if(a[0]=='enter'):
        result=result+int(a[1])
        if(result>max_people[0]):
            count=count+1
            result=result-int(a[1])
    elif(a[0]=='leave'):
        result=result-int(a[1])
print(count)
