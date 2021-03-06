# Matrix Multiplication Algorithms with Python from scratch
Jaeho Kim 
kjh3690@unist.ac.kr

This is an implementation of matrix multiplication algorithm with python. The repository contains a report, code, and a jupyter file. All codes are in python  

1. Schoolbook Matrix multiplication  
1. Naive Divide and Conquer multiplication
1. Strassen
1. Strassen Optimized


## Usage
To run the algorithm you should have a "input.txt" file in the directory where you are running the python scripts.


```bash
# Standard matrix multiplication
python schoolbook_multiplication.py
# Standard naive divide and conquer multiplication
python divide_and_conquer.py
# Standard Strassen 
python strassen_base.py
# Standard Strassen leaf size 4
python strassen_optimized_leaf4.py
# To compare everything and get time_comparison.csv
python all.py
```
There is also a [Jupyter file](https://github.com/jaeho3690/Matrix_multiplication_python/blob/master/Time_complexity.ipynb) to draw graphs.


## Results
![Time complexity for algorithms](/figures/time_complexity.png)
![Time complexity for Strassens](/figures/time_complexity_strassen.png)

## Acknowledgement
It took me so long to figure out why Strassen takes longer implementation time than standard
matrix multiplication even though it has a lower algorithm complexity. To answer this check [stackoverflow](https://stackoverflow.com/questions/11495723/why-is-strassen-matrix-multiplication-so-much-slower-than-standard-matrix-multip). 

Another article you can check out is [here](https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/)

For those who are just to lazy to check out, here is a simple answer. Our standard Strassen makes a recursive call until n equals to 1. This increases the constant time which in theory shouldn't be a problem. But you know, this isn't theory. Its real shiit! So it does matter in reality. We can opimize the time by calling the recusive call until n equals to 2,4,8 ~. Hope someone finds this useful.If I got it wrong please leave a comment on issue! would love to know

Please press star if this was helpful. Thank you
