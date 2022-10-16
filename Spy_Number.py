n=int(input())
s=0
p=1
while n>0:
    a=n%10
    s=s+a
    p=p*a
    n=n//10
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')