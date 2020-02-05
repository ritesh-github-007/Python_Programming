
x=int(input("Enter a no to check for prime"))
prime=0;
for i in range(2,(x//2)+1):
	if x%i==0:
		prime=1
		break
        
if(prime==1):
	print(x," is not a Prime no")
else:
	print(x," is a prime no")
