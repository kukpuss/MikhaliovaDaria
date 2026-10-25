def s(n):
    n=abs(n)
    c=0
    while n>0:
        c+=n%10
        n//=10
    return c

def a(n):
    if not n:
        return None
    return sum(n)/len(n)

def n(t):
    return ' '.join(t.lower().split())

def select_numbers(num, t):
    a = []
    for i in num:
        if i > t:
            a.append(i)
    return a