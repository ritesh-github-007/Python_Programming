n = int(input("Enter a no"))
out=1
def fact(n):

    if(n>1):
       n= n*fact(n-1)
       return n
    else:
        return out

ans = fact(n)
print(ans)
