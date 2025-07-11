# -*- coding: utf-8 -*-
"""Vector operations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10XM76fw2ATWdCcj6_3OKQI_FZYo5cHmU
"""

import numpy as np



a=np.array([2,5])

v=np.array([8,-6])

#magnitude of "v" vector
magnitude_of_v=np.sqrt(sum(v**2))

proj_of_a_on_v=(np.dot(a,v)/magnitude_of_v**2)*v

print('projection of a vector on v vector=', proj_of_a_on_v)



"""Working with numpy as np"""

import numpy as np

#Creating a matrix using numpy
matrix_1=np.array([[2,3],[6,7]])
print(matrix_1)

matrix_1.shape

matrix_2=np.array([[10,35,45],[50,64,80],[20,15,90]])
print(matrix_2)

matrix_2.shape



"""Creating martixes with Random Values"""

random_matrix= np.random.rand(3,3)
print(random_matrix)

random_integer_matrix=np.random.randint(100,size=(4,5))
print(random_integer_matrix)



"""Matrixes with all the values as 1"""

import numpy as np

matrix_3=np.ones((2,3))
print(matrix_3)

matrix_3=np.ones((2,3), dtype=int)
print(matrix_3)

matrix_3=np.ones((10,10), dtype=int)
print(matrix_3)



"""Null matrix"""

null_matrix=np.zeros((4,4))
print(null_matrix)

null_matrix=np.zeros((7,7))
print(null_matrix)



"""identity matrix"""

identity_matrix=np.eye(3,3)
print(identity_matrix)

identity_matrix=np.eye(5,5)
print(identity_matrix)



"""Transpose of a matrix"""

#matrix with random integer values
a=np.random.randint(100, size=(4,5))
print(a)

transpose_of_a=np.transpose(a)
print(transpose_of_a)

