import pandas as pd
import numpy as np
import math


class Matrix_func:
    def __init__(self,matrix_val="dr_teimori"):
        self.matrix_val=matrix_val

    def makematrix2D(self,R,C):
        #ایجاد ماتریس خالی
        matrix=[]
        # حرکت رو سطر
        for i in range(C):          # A for loop for row entries 
            a =[] 
            # حرکت رو ستون
            for j in range(R):      # A for loop for column entries 
                #گرفتن داده ها از ورودی
                 a.append(float(input("Enter matrix C row {} column {} ".format(i,j)))) 
            #درج یک سطر در ماتریس اصلی
            matrix.append(a) 
        #تبدیل ماتریس به numpy
        return np.array(matrix)

    def makematrix1D(self,R):
        #تعریف ماتریس خالی
        a =[]
        # حرکت رو ستون
        for i in range(R):
            # گرفتن داده از ورودی
            a.append(float(input("Enter vector c  column{} ".format(i))))
        # تبدیل وکتور به numpy
        return np.array(a)

    def Tamrine1(self,matrix_C,vector_C,Row,Column):
        #چاپ ماتریس
        print("Matrix C is : -------------")
        print(matrix_C)
        #چاپ وکتور
        print("Vector C is : -------------")
        print(vector_C)
        # ارایه خالی برای همینگ
        haming_distance =[]
        # حرکت در سطر های ماتریس
        for i in range(Row):
            haming_distanc=0
            # حرکت در ستون های یک سطر ماتریس و وکتور
            for j in range(Column):
                # یافتن تفاوت بین ماتریس و وکتور ( یافتن فاصله همینگ )
                if matrix_C[i][j] != vector_C[j]:
                    #+1 اگر برابر نبودن
                    haming_distanc+=1
            #افزودن به ارایه
            haming_distance.append(haming_distanc)
        #چاپ ارایه فاصله همینگ
        print("haming distance matrix_C with vector_c  is : -------------")
        print(haming_distance)
        return haming_distance

    def Tamrine1_Answer(self,haming_distanc):
        min_row=haming_distanc
        min_index_haming=min_row.index(min(min_row)) + 1
        print("minimum haming distanc is in row {}  in Matrix C".format(min_index_haming))
        
    def minlist(self,haming_distanc_list):
        return min(haming_distanc_list)

    def Tamrine2(self,N):
        # ایجاد ارایه خالی
        count_list=[]
        # از 1 شروع تا عدد مورد نظر میرود
        for i in range(1,N+1):
            # اگر باقیمانده تقسیم ان صفر باشد
            if N%i==0:
                # افزودن به ارایه 
                count_list.append(i)
        # چاپ ارایه
        print("list of count N is  :  {}".format(count_list))
        return count_list

    def Tamrine3(self,N):
        prime_list=[]
        count=0
        number=1
        while(count<N):
            if len(self.Tamrine2(number))==2:
                prime_list.append(number)
                count+=1
            number+=1
        print("list of {} prime number  :  {}".format(N,prime_list))
        return prime_list


    def Tamrine4(self,N,K):
        pass


