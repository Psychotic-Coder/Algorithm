# Author: ASHWIN ADARSH github.com/Psychotic-Coder
# This is a Strassen's Matrix Multiplication algorithm for NxN matrix


# This code is my original creation. NOT COPIED

import numpy as np
import math

def matMul(A, B, n):
    R = np.array([[0]*n]*n)
    if n == 1:
        R[0][0] = A[0][0] * B[0][0]
    else:

        A1 = A[:n//2,:n//2]     #Slicing the original array A into 4 equal parts
        A2 = A[:n//2,n//2:]
        A3 = A[n//2:,:n//2]
        A4 = A[n//2:,n//2:]

        B1 = B[:n//2,:n//2]     #Slicing the original array B into 4 equal parts
        B2 = B[:n//2,n//2:]
        B3 = B[n//2:,:n//2]
        B4 = B[n//2:,n//2:]

        P1 = matMul(A1+A4, B1+B4, len(A1))      #Applying Strassen's Formula
        P2 = matMul(A3+A4, B1, len(A1))         #And finding P1..P7
        P3 = matMul(A1, B2-B4, len(A1))
        P4 = matMul(A4, B3-B1, len(A1))
        P5 = matMul(A1+A2, B4, len(A1))
        P6 = matMul(A3-A1, B1+B2, len(A1))
        P7 = matMul(A2-A4, B3+B4, len(A1))

        C1 = ((P1+P4)-P5)+P7        #Creation sub-matrix C
        C2 = P3+P5
        C3 = P2+P4
        C4 = ((P1+P3)-P2)+P6

        R[:len(C1),:len(C1)] = C1       #Combining C1..C4 into result matrix R
        R[:len(C2),len(C2):] = C2
        R[len(C3):,:len(C3)] = C3
        R[len(C4):,len(C4):] = C4

    return R

n = int(input('Size: '))

print('Enter Matrix A')
for _ in range(n):
    temp = list(map(int, input().split(' ')))
    if _ == 0:
        A = np.array([temp])
    else:
        A = np.concatenate((A,[temp]))

print('Enter Matrix B')
for _ in range(n):
    temp = list(map(int, input().split(' ')))
    if _ == 0:
        B = np.array([temp])
    else:
        B = np.concatenate((B,[temp]))

if math.ceil(math.log(n,2)) != math.floor(math.log(n,2)):           #If N is not a power of 2
    next = int(math.pow(2, math.ceil(math.log(n)/math.log(2))))     #next is the nearest power of 2
    
    while(A.shape[0] != next):                                      #Padding 0 to the matrix so that shape is in power of 2
        A = np.concatenate((A,[[0]*n]))
        B = np.concatenate((B,[[0]*n]))
    while(A.shape[1] != next):
        A = np.c_[ A, [0]*next ]
        B = np.c_[ B, [0]*next ]
    R = matMul(A, B, next)
    R = R[:n,:n]                                                    #Slicing the added padding
else:
    R = matMul(A, B, n)
print(R)