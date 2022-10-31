n=int(input())
s=n**2
p=0
while s>0:
    a=s%10
    p=p+a
    s=s//10
if n==p:
    print('Neon Number')
else:
    print('Not Neon Number')