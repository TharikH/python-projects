s1=[]
s2=[]
s3=[]
rep=[]
count=[]
print("enter names: \n ")
s1=raw_input("enter first name\n--")
s2=raw_input("enter second name:\n--")
s3=s1+"loves"+s2
l=len(s3)
for i in range(l-1):
    if(s3[i] not in rep):
        sum=1
        for j in range(i+1,len(s3)):
            if(s3[i]==s3[j]):
                sum+=1
        rep.append(s3[i])
        count.append(sum)
l=len(count)
while(True):
    i=0
    while(i!=l/2):
            count[i]=count[i]+count[l-i-1]
            i+=1
    if(l==2):
        break
    l=(l+1)/2
while(count[0]>9 or count[1]>9):
    if(count[0]>9 and count[1]<=9):
        t=str(count[0])
        count[0]=int(t[0])+count[1]
        count[1]=int(t[1])
    elif(count[1]>9 and count[0]<=9):
        t=str(count[1])
        count[0]=int(t[1])+count[0]
        count[1]=int(t[0])
    else:
        t=str(count[0])
        t1=str(count[1])
        count[0]=int(t[0])+int(t1[1])
        count[1]=int(t[1])+int(t1[0])
print("LOVE percentage is {}{}".format(count[0],count[1]))