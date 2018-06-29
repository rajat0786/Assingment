#ASSIGNMENT 19 NUMPY


#Q1



'''
import numpy as np
a=np.random.randint(1,10,10)
print(a)
print(np.mean(a))



#Q2



import numpy as np
a=np.random.randint(1,20,20)
print(a)
print(np.var(a))
print(np.std(a))



#Q3


import numpy as np
a=np.random.random((10,20))
b=np.random.random((20,25))
x=np.dot(a,b)
print(x)
print(np.sum(x))

'''

#Q4
import numpy as np
a=np.random.randint(1,10,10)
print(a)
for i in a:
    c = 1 / (1 + (-i))
    b=np.array(c)

print(b)

