l=int(input("Enter the array size::"))
num=int(input("Enter an integer number::"))
k=[]
for i in range(2,num+1):
    if(num>1):
        while(num%i==0):
            k.append(i)
            num=num//i
print(k)

q=str(input("Enter the string:"))
k1=[]
q1=int(q[2])
if(q[0]=='!'):
    x=int(q[6])
    r=int(q[4])
    for j in range(0,r):
        
        if(q1==j):
            k1.append(x)
            q1=q1+1
        else:
            k1.append(" ")
    print(k1)
elif(q[0]=='?'):
    start=int(q[2])
    end=int(q[4])
    c=0
    for i in range(start,end+1):
        for j in range(0,len(k)):
            match=int(k[j])
            
            if(match==i):
                if(int(k[j])!=int(k[j-1])):
                    c=c+1
                
    print(c)