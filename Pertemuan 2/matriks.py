import numpy as np

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
c = np.array([[1],
              [4],
              [7]])

d = np.array([[1,4,7]])

print(a+b,'\n')
print(np.dot(a,b),'\n')
print(np.transpose(c),'\n')
print(np.transpose(d),'\n')


