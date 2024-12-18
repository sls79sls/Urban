import numpy as np
#from random import randint
import random

def change_(matrix, column, row):
    for i in range(row,matrix.shape[0]-column):
        for j in range(matrix.shape[1]):
            p = matrix[i][j]
            matrix[i][j] = matrix[row][j]
            matrix[row][j] = p
    return(matrix)

def flip(matrix):
    for i in range(matrix.shape[0]//2):
        for j in range(matrix.shape[1]):
            r = matrix[i][j]
            matrix[i][j] = matrix[matrix.shape[0]-i-1][j]
            matrix[matrix.shape[0]-i-1][j] = r
    return matrix



def transpon(matrix):
    for i in range(matrix.shape[0]):
        for j in range(i+1, matrix.shape[1]):
            a = matrix [i][j]
            matrix [i][j] = matrix[j][i]
            matrix[j][i] = a
    return matrix

def triangl(matrix):
    row = 0
    column = 0
    while column <= matrix.shape[1]-1:
        for i in range(row, matrix.shape[0]-1-column):
            #print(f'matrix[{i}][{k}] = {matrix[i][k]:10.1f}')
            if matrix[i][column] == 0:
                continue
            if matrix[i+1][column] == 0:
                change_(matrix, column, row = i+1)
                if matrix[i+1][column] == 0:
                    continue
            kf = matrix[i][column]/matrix[i+1][column]
            for j in range(matrix.shape[1]):
                matrix[i][j] = matrix[i+1][j] * kf - matrix[i][j]
        column +=1
    return matrix

if __name__ == '__main__':
    d = np.array([[5.0, 3.0, 7.0, 2.0, 9.0], [3.0, 5.0, 7.0, 5.0, 8.0], [1.0, 5.0, 7.0, 4.0, 5.0],
                  [6.0, 6.0, 9.0, 8.0, 9.0], [1.0, 6.0, 6.0, 4.0, 5.0]])
    e = np.random.random(size=(5, 5))
    little = np.array([[5.0,10.0],[15.0,20.0]])
    np.set_printoptions(precision=1, formatter={'float_kind': '{:10.1f}'.format})
    print(d)
    print('------------------num_py_transp------------------------')
    num_py_transp = np.transpose(d, axes=(0,1))
    print(num_py_transp)
    print('------------------My_transp------------------------')
    transpon(d)
    print(d)
    print('-----------------------------------------------------------')
    f = triangl(d)
    print (f)
    print('-----------------------------------------------------------')
    result = flip(f)
    print (result)
    print('---------------------------E------------------------------')
    print(e)
    print('-------------------------triangl-E----------------------')
    print (flip(triangl(e)))
    print('-------------------------little-----------------------')
    print(little)
    print('-------------------------triangl-little--------------------')
    print (flip(triangl(little)))
