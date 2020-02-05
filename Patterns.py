
# *Various Star Patterns* 


#	*
#	**
#	***
#	****
#	*****


for i in range(6):
     for j in range(i):
         print('*',end="")
     print()


print()    #for saperating one pattern from another
print()


# 	*****
# 	****
# 	***
# 	**
# 	*
 

for i in range(5):
     for j in range(5-i):
         print('*', end="")
     print()


print()
print()

 
#	     *
#	    **
#	   ***
#	  ****
#	 *****


for i in range(1,6):
     print(' '*(6-i),end="")
     print('*'*i)
print()


print()
print()


for i in range(1,6):
     print('*'*i)

 
print()
print()


# diamond pattern
'''
     **
    ****
   ******
  ********
 **********
**********
 ********
  ******
   ****
    **
'''

for i in range(1,6):
     print(' '*(6-i),end="")
     print('*'*(i*2))

for i in range(0,5):
     print(' '*i,end="")
     print('*'*((5-i)*2))





