def fib(n):     #iteracyjna
    a=0 #n-2
    b=1 #n-1
    for _ in range(n):
        c=a+b
        a=b     #a,b==b,a
        b=c
    return a
print(fib(35))

def fib_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(35))