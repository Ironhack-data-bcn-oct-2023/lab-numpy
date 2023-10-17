#1. Import the NUMPY package under the name np.

import numpy as np
print("hell world")


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.randint(0, 10, (2,3,5))

from numpy import random
a_2 = random.randint(10, size=(2,3,5))

a_3 = np.round(random.rand(2, 3, 5)*10,0)



#4. Print a.
print(a)
print(a_2)
print(a_3)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))


#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
#a and b do have the same size
if a.size == b.size:
    print("Yes. See? I told you")
else:
    print("diff sizes, different colours but we are all equal inside")


#8. Are you able to add a and b? Why or why not?
#No, I'll get an error "ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) "
#Even though same size, different shapes. We have to boradcast them to the same shape.


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
#we want (5,2,3) -->(2,3,5) 
#IMPORTANT FOR ME TO UNDERSTAND, logic is: (thank you Lucia)
#looking at the shape of the goal matrix, which position does each element occupy in the current shape?
print(f"current shape is {b.shape}")
print(f"goal shape is {a.shape}")
c = b.transpose(1,2,0)
print(f"in the goal shape, {a.shape}, the 2 occupies current position -1- in the current structur [{b.shape}]so this is the first element in the method, then the 3 occupies currently -2-, then the 5 occupies currently -0-")
print(c.shape)



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add(a,c)
print(d)
#Works because it works.Period.
#Works because the first matrix has got a corresponding (matching) position to add each of its elements to.


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)
#not sure what is meant with this question but if I'm not addressing it please let me know what you were going after!
#"d" is simply the first matrix "a" where each of its values have an increment of 1 (the values in the ones matrix c)
#they have the same shape after the transposition of c. 



#12. Multiply a and c. Assign the result to e.
print(a.shape)
print(c.shape)
e = np.multiply(a,c)
print(e)


#13. Does e equal to a? Why or why not?
#yes, we've basically multiplied the a matrix by 1 (which is the value for every element in matrix c)
#it's as if we were multiplying the matrix a by a scalar 1.
#we can check that every element returns True for the comparison of both matrices:
print(a == e)


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = d.max()
d_min = d.min()
d_mean = d.mean()



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
farray = np.empty((d.shape))
print(farray)



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
#Was trying this but last 3 conditions were reseting th2 first two:
"""
#first rule: if it's larger than d_min but smaller than d_mean, assign 25 
#f = np.where(np.logical_and(d > d_min, d < d_mean), 25, d)

#second rule: larger than d_mean but smaller than d_max, assign 75
#f = np.where(np.logical_and(d > d_mean, d < d_max), 75, d)

#third rule: value equals to d_mean, assign 50 to the corresponding value in f
#f = np.where(d == d_mean, 50, d)

#fourth rule:  0 to the corresponding value(s) in f for d_min in d
#f = np.where(d < d_min, 0, d)

#fifth rule:  100 to the corresponding value(s) in f for d_max in d.
#f = np.where(d > d_max, 100, d)
"""

#so here's the deal:

f = np.where((d > d_min) & (d < d_mean), 25,
             np.where((d > d_mean) & (d < d_max), 75,
                      np.where(d == d_mean, 50,
                               np.where(d <= d_min, 0,
                                        np.where(d >= d_max, 100, d)))))
print(f)

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
#YES. Fuck yes.

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

#sort of the same thing, just changing the outputs, innit?
f = np.where((d > d_min) & (d < d_mean), "B",
             np.where((d > d_mean) & (d < d_max), "D",
                      np.where(d == d_mean, "C",
                               np.where(d <= d_min, "A",
                                        np.where(d >= d_max, "D", d)))))

print(f)