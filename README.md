# Matrix Multiplication Algorithms with Python from scratch

This is an implementation of matrix multiplication algorithm with python. 

1. Schoolbook Matrix multiplication  
1. Naive Divide and Conquer multiplication
1. Strassen


## Usage

```bash
# Set configuration. Change the following file for your directory, hyperparameters. This configuration file will generate "lung.conf"
python config_file_create.py
# We then prepare the dataset. 
python prepare_dataset.py
# After creating all the dataset, run train_unet.py
python train_unet.py

```


## Acknowledgement
It took me so long to figure out why Strassen takes longer implementation time than standard
matrix multiplication even though it has a lower algorithm complexity. To answer this I found out a well written answer in [stackoverflow](https://stackoverflow.com/questions/11495723/why-is-strassen-matrix-multiplication-so-much-slower-than-standard-matrix-multip). 

Another article you can check out is [here](https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/)

For those who are just to lazy to check out, here is a simple answer. Our standard Strassen makes a recursive call until n equals to 1. This increases the constant time which in theory shouldn't be a problem. But you know, this isn't theory. Its real shiit! So it does matter in reality. We can opimize the time by calling the recusive call until n equals to 2,4,8 ~. Hope someone finds this useful.
