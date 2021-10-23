# a=int(input("ask something"))
# b=int(input("ask something"))

def findValue(a,b):
    if a==b:
        print("Yes")
        return 1
    else:
        while b>0:
            r1=a%10
            r2=b%10
            if r1!=r2:
                x=True        
            a=a//10
            b=b//10  
        if x:
            print("No")
            return 0
        else:
            print("Yes") 
            return 1       
print(findValue(1234,1234))