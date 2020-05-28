def readData():
    s=0
    with open("test.txt","r") as f:
        for string in f:
            temp=""
            for i in range(len(string)-2,-1,-1):
                if(string[i]==' '):
                    break
                temp=string[i]+temp
            s=sums(s,int(temp))
        return(s)


sums=lambda a,b: a+b

def writeData():
    with open("test.txt","w") as f:
        for _ in range(2):
            name=raw_input("Enter name: ")
            roll=raw_input("enter roll: ")
            string=name+" roll number is "+roll+"\n"
            f.writelines(string)

writeData()
print(readData())