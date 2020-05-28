smalls=(lambda a,b: a if a<b else b)
larges=(lambda a,b:a if a>b else b)
i=1
while(i):
    ch=raw_input("enter number")
    try:
        if(ch=="done"):
            break
        temp=int(ch)
        if (i==1):
            small=temp
            large=temp
        else:
            small=smalls(small,temp)
            large=larges(large,temp)
        i+=1
    except:
        print("invalid number")
print("largest is {}\nsmallest is {}".format(large,small))