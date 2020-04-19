import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd 

def create_test_case():
    input_size = [2 ** i for i in range(1,12)]
    log= pd.DataFrame(index=[],columns= ['Array_size','Schoolbook_time','Divide_Conquer_time','Divide_Conquer_time2','Strassen_time','Strassen_optimized_2','Strassen_optimized_4'])
    print(input_size)
    for size in input_size:
        print(size)
        #Initialize random array with size corresponding to the power of 2
        array_1 = np.random.randint(low=-100,high=100,size=(size,size),dtype=int)
        array_2 = np.random.randint(low=-100,high=100,size=(size,size),dtype=int)
        
        # Test school book algorithm
        print("Testing School Book size {}".format(size))
        start_time = 0
        start_time = time.time()
        result = schoolbook2(array_1,array_2)
        schoolbook_duration = time.time()-start_time
        #print(result)
        
        # Divide and conquer
        print("Testing Divide and conquer size {}".format(size))
        start_time = 0
        start_time = time.time()        
        result = divide_and_conquer(array_1,array_2)
        divide_and_conquer_duration = time.time()-start_time
        #print(result)

        # Divide and conquer2
        print("Testing Divide and conquer 2 size {}".format(size))
        start_time = 0
        start_time = time.time()        
        result = divide_and_conquer2(array_1,array_2)
        divide_and_conquer_duration2 = time.time()-start_time
        
        # Strassen
        print("Testing Strassen size {}".format(size))
        start_time = 0
        start_time = time.time()
        result = strassen(array_1,array_2)
        strassen_duration = time.time()-start_time
        
        # Strassen_optimized_leaf2
        print("Testing Strassen optimized 2 size {}".format(size))
        start_time = 0
        start_time = time.time()
        result = strassen_optimized_leaf2(array_1,array_2)
        strassen_duration_optimized_2 = time.time()-start_time

        # Strassen_optimized_leaf4
        print("Testing Strassen optimized 4 size {}".format(size))
        start_time = 0
        start_time = time.time()
        result = strassen_optimized_leaf_4(array_1,array_2)
        strassen_duration_optimized_4 = time.time()-start_time
        
        print("SCHOOL BOOK:{}, DIVIDE AND CONQUER:{}, DIVIDE AND CONQUER2:{}, STRASSEN:{}, STRASSEN OPTIMIZED_2:{}, STRASSEN OPTIMIZED_4:{}".format(schoolbook_duration,
                                                                          divide_and_conquer_duration, divide_and_conquer_duration2, strassen_duration,strassen_duration_optimized_2,strassen_duration_optimized_4))
        
        tmp = pd.Series([
            size,
            schoolbook_duration,
            divide_and_conquer_duration,
            divide_and_conquer_duration2,
            strassen_duration,
            strassen_duration_optimized_2,
            strassen_duration_optimized_4
        ], index=['Array_size','Schoolbook_time','Divide_Conquer_time','Divide_Conquer_time2','Strassen_time','Strassen_optimized_2','Strassen_optimized_4'])
        log = log.append(tmp,ignore_index=True)
        log.to_csv('new_time_complexity_python.csv',index=False)
    return log 
        

def read_input(input):
    array = np.loadtxt(input,dtype='i',delimiter=' ')
    #Seperate array
    array_first,array_second = np.split(array,2,axis=0)
    return array_first, array_second 

def schoolbook(array_first,array_second):
    #print("SCHOOL BOOK Implementation")
    #Create empty matrix to use it as return matrix
    result = np.zeros_like(array_first)
    for row_idx, row in enumerate(array_first):
        for i in range(len(row)):
            for cell_idx, cell in enumerate(row):
                result[row_idx,i]+= cell * array_second[cell_idx,i]
    return result

def schoolbook2(array_first,array_second):
    n = len(array_first)
    result = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i,j] += array_first[i,k] *array_second[k,j]
    return result



def divide_and_conquer(array_first,array_second):
    n = len(array_first)
    if n == 1:
        return array_first * array_second
    else:
        a11 = array_first[:int(len(array_first)/2),:int(len(array_first)/2)]
        a12 = array_first[:int(len(array_first)/2),int(len(array_first)/2):]
        a21 = array_first[int(len(array_first)/2):,:int(len(array_first)/2)]
        a22 = array_first[int(len(array_first)/2):,int(len(array_first)/2):]

        b11 = array_second[:int(len(array_second)/2),:int(len(array_second)/2)]
        b12 = array_second[:int(len(array_second)/2),int(len(array_second)/2):]
        b21 = array_second[int(len(array_second)/2):,:int(len(array_second)/2)]
        b22 = array_second[int(len(array_second)/2):,int(len(array_second)/2):]

        c11 = divide_and_conquer(a11,b11) + divide_and_conquer(a12,b21)
        c12 = divide_and_conquer(a11,b12) + divide_and_conquer(a12,b22)
        c21 = divide_and_conquer(a21,b11) + divide_and_conquer(a22,b21)
        c22 = divide_and_conquer(a21,b12) + divide_and_conquer(a22,b22)

        result = np.zeros((n,n))
        result[:int(len(result)/2),:int(len(result)/2)] = c11
        result[:int(len(result)/2),int(len(result)/2):] = c12
        result[int(len(result)/2):,:int(len(result)/2)] = c21
        result[int(len(result)/2):,int(len(result)/2):] = c22
        #print("Divide and Conquer")
    return result

def divide_and_conquer2(array_first,array_second):
    n = len(array_first)
    if n <= 4:
        return schoolbook2(array_first,array_second)
    else:
        a11 = array_first[:int(len(array_first)/2),:int(len(array_first)/2)]
        a12 = array_first[:int(len(array_first)/2),int(len(array_first)/2):]
        a21 = array_first[int(len(array_first)/2):,:int(len(array_first)/2)]
        a22 = array_first[int(len(array_first)/2):,int(len(array_first)/2):]

        b11 = array_second[:int(len(array_second)/2),:int(len(array_second)/2)]
        b12 = array_second[:int(len(array_second)/2),int(len(array_second)/2):]
        b21 = array_second[int(len(array_second)/2):,:int(len(array_second)/2)]
        b22 = array_second[int(len(array_second)/2):,int(len(array_second)/2):]

        c11 = divide_and_conquer2(a11,b11) + divide_and_conquer2(a12,b21)
        c12 = divide_and_conquer2(a11,b12) + divide_and_conquer2(a12,b22)
        c21 = divide_and_conquer2(a21,b11) + divide_and_conquer2(a22,b21)
        c22 = divide_and_conquer2(a21,b12) + divide_and_conquer2(a22,b22)

        result = np.zeros((n,n))
        result[:int(len(result)/2),:int(len(result)/2)] = c11
        result[:int(len(result)/2),int(len(result)/2):] = c12
        result[int(len(result)/2):,:int(len(result)/2)] = c21
        result[int(len(result)/2):,int(len(result)/2):] = c22
        #print("Divide and Conquer")
    return result

def strassen(array_first,array_second):
    n = len(array_first)
    if n == 1:
        return array_first * array_second
    else:
        a11 = array_first[:int(len(array_first)/2),:int(len(array_first)/2)]
        a12 = array_first[:int(len(array_first)/2),int(len(array_first)/2):]
        a21 = array_first[int(len(array_first)/2):,:int(len(array_first)/2)]
        a22 = array_first[int(len(array_first)/2):,int(len(array_first)/2):]

        b11 = array_second[:int(len(array_second)/2),:int(len(array_second)/2)]
        b12 = array_second[:int(len(array_second)/2),int(len(array_second)/2):]
        b21 = array_second[int(len(array_second)/2):,:int(len(array_second)/2)]
        b22 = array_second[int(len(array_second)/2):,int(len(array_second)/2):]

        S1 = b12 - b22
        S2 = a11 + a12
        S3 = a21 + a22
        S4 = b21 - b11
        S5 = a11 + a22
        S6 = b11 + b22
        S7 = a12 - a22
        S8 = b21 + b22
        S9 = a11 - a21
        S10 = b11 + b12
        
        P1 = strassen(a11,S1)
        P2 = strassen(S2,b22)
        P3 = strassen(S3,b11)
        P4 = strassen(a22,S4)
        P5 = strassen(S5,S6)
        P6 = strassen(S7,S8)
        P7 = strassen(S9,S10)
        
        c11 = P5 +P4 -P2 +P6
        c12 = P1 +P2
        c21 = P3 +P4
        c22 = P5 +P1 -P3 -P7

        result = np.zeros((n,n))
        result[:int(len(result)/2),:int(len(result)/2)] = c11
        result[:int(len(result)/2),int(len(result)/2):] = c12
        result[int(len(result)/2):,:int(len(result)/2)] = c21
        result[int(len(result)/2):,int(len(result)/2):] = c22
        return result


def strassen_optimized_leaf2(array_first,array_second):
    n = len(array_first)
    if n <= 2:
        return schoolbook2(array_first,array_second)
    else:
        a11 = array_first[:int(len(array_first)/2),:int(len(array_first)/2)]
        a12 = array_first[:int(len(array_first)/2),int(len(array_first)/2):]
        a21 = array_first[int(len(array_first)/2):,:int(len(array_first)/2)]
        a22 = array_first[int(len(array_first)/2):,int(len(array_first)/2):]

        b11 = array_second[:int(len(array_second)/2),:int(len(array_second)/2)]
        b12 = array_second[:int(len(array_second)/2),int(len(array_second)/2):]
        b21 = array_second[int(len(array_second)/2):,:int(len(array_second)/2)]
        b22 = array_second[int(len(array_second)/2):,int(len(array_second)/2):]
        
        P1 = strassen_optimized_leaf2(a11,b12 - b22)
        P2 = strassen_optimized_leaf2(a11 + a12,b22)
        P3 = strassen_optimized_leaf2(a21 + a22,b11)
        P4 = strassen_optimized_leaf2(a22,b21 - b11)
        P5 = strassen_optimized_leaf2(a11 + a22,b11 + b22)
        P6 = strassen_optimized_leaf2(a12 - a22,b21 + b22)
        P7 = strassen_optimized_leaf2(a11 - a21,b11 + b12)

        result = np.zeros((n,n))
        result[:int(len(result)/2),:int(len(result)/2)] = P5 +P4 -P2 +P6
        result[:int(len(result)/2),int(len(result)/2):] = P1 +P2
        result[int(len(result)/2):,:int(len(result)/2)] = P3 +P4
        result[int(len(result)/2):,int(len(result)/2):] = P5 +P1 -P3 -P7
        return result

def strassen_optimized_leaf_4(array_first,array_second):
    n = len(array_first)
    if n <= 4:
        return schoolbook2(array_first,array_second)
    else:
        a11 = array_first[:int(len(array_first)/2),:int(len(array_first)/2)]
        a12 = array_first[:int(len(array_first)/2),int(len(array_first)/2):]
        a21 = array_first[int(len(array_first)/2):,:int(len(array_first)/2)]
        a22 = array_first[int(len(array_first)/2):,int(len(array_first)/2):]

        b11 = array_second[:int(len(array_second)/2),:int(len(array_second)/2)]
        b12 = array_second[:int(len(array_second)/2),int(len(array_second)/2):]
        b21 = array_second[int(len(array_second)/2):,:int(len(array_second)/2)]
        b22 = array_second[int(len(array_second)/2):,int(len(array_second)/2):]
        
        P1 = strassen_optimized_leaf_4(a11,b12 - b22)
        P2 = strassen_optimized_leaf_4(a11 + a12,b22)
        P3 = strassen_optimized_leaf_4(a21 + a22,b11)
        P4 = strassen_optimized_leaf_4(a22,b21 - b11)
        P5 = strassen_optimized_leaf_4(a11 + a22,b11 + b22)
        P6 = strassen_optimized_leaf_4(a12 - a22,b21 + b22)
        P7 = strassen_optimized_leaf_4(a11 - a21,b11 + b12)

        result = np.zeros((n,n))
        result[:int(len(result)/2),:int(len(result)/2)] = P5 +P4 -P2 +P6
        result[:int(len(result)/2),int(len(result)/2):] = P1 +P2
        result[int(len(result)/2):,:int(len(result)/2)] = P3 +P4
        result[int(len(result)/2):,int(len(result)/2):] = P5 +P1 -P3 -P7
        return result


if __name__ == "__main__":
    log = create_test_case()
