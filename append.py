import numpy as np
x=input("enter array1:")
y=input("enter array2:")
print "1st array is",np.array(x)
print "2nd array is",np.array(y)
i=0
while i<len(y):
	x=np.append(x,y[i])
	i=i+1 
print "after appending array is",x

