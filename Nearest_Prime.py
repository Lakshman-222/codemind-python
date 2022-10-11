x=int(input())
for j in range(x):
    n=int(input())
    a=n
    b=n
    while True:
        s=0
        for i in range(1,a+1):
            if a%i==0:
                s+=1
        if s==2:
            break
        a-=1
    while True:
        s=0
        for i in range(1,b+1):
            if b%i==0:
                s+=1
        if s==2:
            break
        b+=1
    if n-a<=b-n:
        print(a)
    else:
        print(b)
            