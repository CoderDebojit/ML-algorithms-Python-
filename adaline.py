x1=[1,1,1,1,-1,-1,-1,-1]
x2=[1,1,-1,-1,1,1,-1,-1]
x3=[1,-1,1,-1,1,-1,1,-1]
t=[1,-1,1,-1,1,-1,1,-1]

l=len(x1)
yin,yout=[],[]
#initialy set the weight
w0,w1,w2,w3,b=0,0.2,0.1,0.5,0.3
daltaw1,daltaw2,daltaw3=[],[],[]
weight1,weight2,weight3=[],[],[]
error=[]
#where w0=bias weight,w1=x1 weight, w2=x2 weight, w3=x3 weight, b=bias value
a=0.1 #larning rate
epoc=int(input("Enter how many epoc you want:"))
f=0
while True:
    for i in range(0,l):
        yin.append(w0*b+w1*x1[i]+w2*x2[i]+w3*x3[i])
        error.append(t[i]-yin[i])
        w0=w0+a*(t[i]-yin[i])
        w1=w1+a*(t[i]-yin[i])*x1[i]
        w2=w2+a*(t[i]-yin[i])*x2[i]
        w3=w3+a*(t[i]-yin[i])*x3[i]
        #b=b+a*(t[i]-yin[i])
        weight1.append(w1)
        weight2.append(w2)
        weight3.append(w3)
        daltaw1.append(a*(t[i]-(yin[i]))*x1[i])
        daltaw2.append(a*(t[i]-(yin[i]))*x2[i])
        daltaw3.append(a*(t[i]-(yin[i]))*x3[i])
        #activation function
        if(yin[i]>=0):
            yout.append(1)
        elif(yin[i]<0):
            yout.append(-1)
    f+=1
    if(f==epoc):
        break
print("Weight1 are change:",weight1)
print("Weight2 are change:",weight2)
print("Weight3 are change:",weight3)
print("DaltaWeight1 are change:",daltaw1)
print("DaltaWeight2 are change:",daltaw2)
print("DaltaWeight3 are change:",daltaw3)
print("Errors:",error)
print("Pradicted out put:",yout)