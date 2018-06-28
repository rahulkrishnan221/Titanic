import numpy as np
#creating Array
myList=[1,2,3]
x=np.array(myList)
print(x)
#multiarray
y=np.array(myList)
m=np.array([x,y])
#for size
m.shape
#for array with value start,stop,step size
n=np.arange(0,30,2)
#for reshaping the array
n=n.reshape(3,5)
#linespace is similar to arrange but in this we have 
#start stop number of output number so it split accordingly
o=np.linespace(0,4,9)
#for resize
m.resize(2,3)
#returns a new array of given shape and type, filled with ones
np.ones((3, 2))
#zeros returns a new array of given shape and type, filled with zeros.
np.zeros((2, 3))
#eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
np.eye(3)
#diag extracts a diagonal or constructs a diagonal array.
np.diag(y)
#Create an array using repeating list
np.array([1, 2, 3] * 3)
#Repeat elements of an array using repeat.
np.repeat([1, 2, 3], 3)
#combining verticlly
np.vstack([p, 2*p])
#combining horizontally
np.hstack([p, 2*p])
#arithematic operation on two array is done using simply +,-,*,/,**
#for dot product
x.dot(y)
#for transpose
x.T
# .dtype is used to see what type
x.dtype
#to cast to other type
x=x.astype('f')

#Math Function
#for sum of all matrix element
a.sum()
#max
a.max()
#min
a.min()
#mean
a.mean()
#standard deviation
a.std()
#argmax and argmin return the index of the maximum and minimum values in the array.
a.argmax()
a.argmin()
#for square of matrix as arrange give value upto 13 1......13
s=np.arrange(13)**2
#result=[0,1,4,9,16,25........144]
#slicing
s[0],s[4],s[0:3],s[-1]
#[start:stop:step]
#getting value for the particular index
s[1,2]
#below is 3 row and 3 column to 5
s[3,3:6]
#also we can have result for arrange(36) [0.......10]
r[:2,:-1]
#every second in the last row
r[-1,::2]
#condition operation==[31.......35]
r[r>30]
#make all 30 if >30
r[r>30]=30
#be aware during copying in numpy arrar
#example
r2=r[:3,:3]
r2[:]=0
#hence r also get changed because of change of r2
#due to copy
#to avoid this we can use like this
r_copy=r.copy()
#copy function only copy it
# create a new 4 by 3 array of random numbers 0-9.
test=np.random.randint(0,10,(4,3))
#iterate by row
for row in test:
	print(row)
#iterate by index
for i in range(len(test)):
    print(test[i])
#Iterate by row and index: using enumerate
for i, row in enumerate(test):
    print('row', i, 'is', row)
 #For iterating between both the array we have zip
 for i,j in zip(x,y):
 	print(i,j)
 	
