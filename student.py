def swaps(s,a,b):
    temp=s[a]
    s[a]=s[b]
    s[b]=temp
def swap(s,a,b):
    for i in range(6):
        swaps(s,a,b)
        a-=1
        b-=1
s=[]
n=input("enter how many students\n")
for j in range(n):
    i=raw_input("enter name: ")
    s.append(i)
    i=input("enter roll: ")
    s.append(i)
    s1=input("enter 1st mark: ")
    s.append(s1)
    s2=input("enter 2nd: ")
    s.append(s2)
    s3=input("enter third number: ")
    s.append(s3)
    i=(s1+s2+s3)/3
    s.append(i)
for i in range(5,n*5,6):
    for j in range(i+6,n*6,6):
        if(s[i]<s[j]):
            swap(s,i,j)
f=open("students.txt","w")
for i in range(n*6-1):
    if((i+1)%6==0):
        continue
    f.write(str(s[i])+"\n")
f.close()