import pandas as pd
import numpy as np
from Matrix_func import Matrix_func

matrix_function =Matrix_func()

question=input("Which question do you want solve? ")

if question=="1":
    #Tamrine 1 : find haming distance between matrix c and vector c
    R = int(input("Enter the number of rows:")) 
    C = int(input("Enter the number of columns:")) 
    a=matrix_function.makematrix2D(R,C)
    b=matrix_function.makematrix1D(R)
    haming_des=matrix_function.Tamrine1(a,b,R,C)
    matrix_function.Tamrine1_Answer(haming_des)
elif question=="2":
    #tamrine 2 : find counter in N 
    N=int(input("Enter the number:")) 
    matrix_function.Tamrine2(N)
elif question=="3":
    #tamrine 3 : find N minimum Prime number
    N=int(input("Enter the count of prime number:")) 
    matrix_function.Tamrine3(N)
elif question=="4":
    #tamrine 4 : solve function with n value equal with k
    n = int(input("Enter n:")) 
    k = int(input("Enter k:")) 
    matrix_function.Tamrine4(n,k)




