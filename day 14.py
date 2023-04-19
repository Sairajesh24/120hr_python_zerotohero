#fibo
def fibo(n):
    a=0
    b=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=5
s=0
for i in range(n+1):
    x=fibo(i)
    print(x,end=",")
    s=s+x
print("\ntotal:",s)
#
