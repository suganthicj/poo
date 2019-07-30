x11=int(input())
y11=""
for i in range(1,x11+1):
    if x11%i==0 and i%2==1:
        y11=y11+str(i)+" "
print(y11.strip())
