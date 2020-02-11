MAX=1000
def factor(n):
    k=0
    for i in range(1,n):
        if(n%i==0):
            k+=i
    return k
for i in range(1,MAX):
    k=factor(i)

    if(k==i):
        print(i)





