import numpy as np
#operations of linear algebra 
print ("Operations on Arrays")
x=input("enter 3*3 matrix1:")
y=input("enter 3*3 matrix2:")
a=np.asarray(x)
b=np.asarray(y)
print "array1 is:\n",a
print "array2 is:\n",b
#operatins on arrays by using numpy
#on single matrix
print "determinant of matrix is",np.linalg.det(a)
print "trace of matrix is",np.trace(a)
print "inverse of matrix is",np.linalg.inv(a)
print "rank of matrix is",np.linalg.matrix_rank(a)
print "power of matrix is",np.linalg.matrix_power(a,4)
print "diagonal elements of matrix is",np.diagonal(a)
print "eigen values of matrix",np.linalg.eig(a)
print "transpose of matrix is",np.transpose(a)
print "maximum value of matrix",np.max(a)
print "minimum value of matrix",np.min(a)
#on two matrices
print "addition of matrices x and y is",np.add(a,b)
print "substraction of matrices x and y is",np.subtract(a,b)
print "multiplication of matrices x and y is",np.dot(a,b)
print "division of matrices x and y is",np.divide(a,b)
print "linear solution is",np.linalg.solve(a,b)


