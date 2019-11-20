b = int(input())
t = int(input())
for i in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    s=0
    while n>3:
        s += min((a[0]+2*a[1]+a[n-1]),(a[n-2]+a[n-1]+2*a[0]))
        n -=2
    if n==3:
        s=s+a[0]+a[1]+a[2]
    elif n==2:
        s=s+a[1]
    elif n==1:
        s=s+a[0]
    
    print(s)
