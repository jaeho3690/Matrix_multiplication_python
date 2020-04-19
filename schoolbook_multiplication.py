"""20161349 JaehoKim
Intro to Algorithms Schoolbook matrix multiplication""" 

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





if __name__ == "__main__":
    array_first,array_second = read_input('input.txt')
    output = schoolbook(array_first,array_second)
    save_ouput(output)