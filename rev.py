def length(a):
    c=0
    while(a!=0):
        c+=1
        a=a//10
    return c
n=int(input("enter number"))
lastdig=n%10
c=length(n)
firstdig=n//(10**(c-1))
n=n-lastdig+firstdig
p=n%(10**(c-1))
n=lastdig*(10**(c-1))+p
print(n)