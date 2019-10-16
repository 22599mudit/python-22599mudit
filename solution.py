def cz(n,c=0):
    if n>0:
        a=n%10
        if a!=0:
            return cz(n//10,c)
        elif a==0:
            return cz(n//10,c+1)
    else:
        return c
n=int(input("enter an integer"))
print(cz(n))
