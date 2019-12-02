import random
x=[] 
u1,u2,u=[],[],[]
m=2
d=int(input("How many data point:"))
print("\nEnter the datas:")
for i in range(0,d):
    x.append(int(input()))
#member ship values
for i in range(0,len(x)):
    u1.append(random.uniform(0.1,0.9))
    u2.append(1-u1[i])
u.append(u1)
u.append(u2)

t1,t2,t3,t4=[],[],[],[]
f=0
t_c1,t_c2=[],[]
new_c1,new_u_c1,new_u_c2=[],[],[]
#epoc=int(input("Enter the epoc:"))
while True:
    for i in range(0,len(x)):
        t1.append(((u1[i])**m)*x[i])
        t2.append(u1[i]**m)   
        t3.append(((u2[i])**m)*x[i])
        t4.append(u2[i]**m)
    sum_up_c1=sum(t1)
    sum_dp_c1=sum(t2)
    sum_up_c2=sum(t3)
    sum_dp_c2=sum(t4)
    
    c1=sum_up_c1/sum_dp_c1
    
    c2=sum_up_c2/sum_dp_c2
    t_c1.append(c1)
    t_c2.append(c2)
    f+=1
    for i in range(0,len(x)):
        new_u_c1.append(1/(((abs(x[i]-c1))/abs(x[i]-c1))**2+((abs(x[i]-c1))/abs(x[i]-c2))**2))
        new_u_c2.append(1/(((abs(x[i]-c2))/abs(x[i]-c1))**2+((abs(x[i]-c2))/abs(x[i]-c2))**2))
    new_c1.append(new_u_c1)
    new_c1.append(new_u_c2)
    if(new_u_c1[i]-u1[i]<0.01 and new_u_c2[i]-u2[i]<0.01):
        #print("eq")
        break
    u1.clear()
    u2.clear()
    
    u1=new_u_c1
    u2=new_u_c2

c1_d,c2_d=[],[]

for i in range(0,len(x)):
    if(new_u_c1[i]>new_u_c2[i]):
        c1_d.append(x[i])
    elif(new_u_c1[i]<new_u_c2[i]):
        c2_d.append(x[i])
out=[]
for i in range(0,len(x)):
    out.append(new_u_c1[i]+new_u_c2[i])
print("Total number of epoc is=",f)
print("centroid1=",c1)
print("centroid2=",c2)
print("claster1=",c1_d)
print("claster2=",c2_d)
print(new_u_c1,new_u_c2)
print(out)