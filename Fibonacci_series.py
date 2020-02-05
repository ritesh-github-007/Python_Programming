

x=int(input("How many terms do you want in Fibonacci sequence?"))
count=0
n1=0
n2=1
nth=0

while count<=x:
    print(n1, end=" , ")
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
