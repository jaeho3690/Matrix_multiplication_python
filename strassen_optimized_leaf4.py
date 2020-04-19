"""20161349 JaehoKim
Intro to Algorithms Strassen with Leaf size 4""" 

#Import Libray. I only used numpy for numpy array. None of the functions implemented in numpy has been used during matrix calculations
import numpy as np
import time

def read_input(input):
    """ Both inputs are stored in the input.txt file """
    array = np.loadtxt(input,dtype='i',delimiter=' ')
    #Seperate array
    array_first,array_second = np.split(array,2,axis=0)
    return array_first, array_second 

def save_ouput(output):
    output_array = np.savetxt("output.txt",output,delimiter=' ')

def schoolbook(array_first,array_second):
    """This is the standard matrix multiplication O(n^3)"""
    n = len(array_first)
    result = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i,j] += array_first[i,k] *array_second[k,j]
    return result

def strassen_optimized_leaf_4(array_first,array_second):
    n = len(array_first)
    if n <= 4:
        return schoolbook(array_first,array_second)
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
    array_first,array_second = read_input('input.txt')
    start_time = time.time()
    output = strassen_optimized_leaf_4(array_first,array_second)
    print("TIME TAKEN: ",time.time()-start_time)
    save_ouput(output)