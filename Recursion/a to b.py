def sum(a,b):
    if a==b:
        return a
    if a>b:
        return 0
    m = (a+b)//2
    return sum(a,m) + sum(m+1,b)

print(sum(2,7))