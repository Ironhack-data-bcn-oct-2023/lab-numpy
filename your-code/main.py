#1. Import the NUMPY package under the name np.
import numpy as np
import random

def numpy_info (array):
    print(f"The type is {type(array)}")
    print(f"The n.dim is {array.ndim}")
    print(f"The shape is {array.shape}")
    print(f"The size is {array.size}")


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config)



#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(100, size = (2, 3, 5))
numpy_info(a)
a_1 = np.random.rand(2, 3, 5)
numpy_info(a_1)
a_2 = np.random.choice(100, size= (2, 3, 5))
numpy_info(a_2)

#4. Print a.
print(a_1)
print(a_2)
print(a_2)



#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5, 2, 3))
numpy_info(b)


#6. Print b.
print(b)




#7. Do a and b have the same size? How do you prove that in Python code?
a.size == b.size
print(a.size)
print(b.size)




#8. Are you able to add a and b? Why or why not?
# a + b  -> ValueError
#We cannot add a + b because even though the size is the same, the shape is not so in order to be able to aperate between those arrays, we'd need to transpose.



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
print(a.shape)
print(b.shape)

c = b.transpose(1, 2, 0)
print(c.shape)



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
print(d)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)
'''as c was a ones array, when we changed the shape, we could superpose the both of them and do the addition.
This is why the values are the innitial ones +1. 
But we can also observe that the d array has a dot after each value, I think that happens because normally
an array of ones as an array of 0 are used to create masks aka a filter to an array with a condition to return True or false
and only show the True ones, that is when the condition is met'''


#12. Multiply a and c. Assign the result to e.

e = a * c
print(e)
print(a)
numpy_info(e)
numpy_info(a)


#13. Does e equal to a? Why or why not?

a == e 

''' Yes, because it e equals a, the first array multiplied with c, the ones mask, so basically you are passing a mask of always true.
Also c is a ones array, so it multiplies per one. I don't know if that means that e becomes a mask, because of the dots?'''


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
print(d_max)

d_min= np.min(d)
print(d_min)

d_mean = np.mean(d)
print(d_mean)



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2, 3, 5))
print(f)
numpy_info(f)

#The result say that f == e and f == d

f == e



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
'''f = np.where( d_min < d < d_mean, 25)
f = np.where(d == d_mean, 50)
f = np.where(d == d_min , 0)
f = np.where(d == d_max, 100)

f[d_min < d < d_mean] = 25
f.all(d_min < d < d_mean, 25)'''

f[(d_min < d) & ( d < d_mean) ] = 25
f[(d_mean < d) & ( d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min ] = 0
f[d == d_max] = 100

print(f)

'''

f = list(f.flatten())
print(f)

for i in f:
        i = int(i)
        if d_min < d < d_mean:
                i = 25
        elif d == d_mean:
                i = 50
        elif d == d_min:
                i = 0
        else:
                i = 100

print(f)
'''





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
print(d)
print(f)

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

h = np.empty((2, 3, 5), dtype=str)
print(h)

h[(d_min < d) & ( d < d_mean) ] = "B"
h[(d_mean < d) & ( d < d_max)] = "D"
h[d == d_mean] = "C"
h[d == d_min ] = "A"
h[d == d_max] = "E"

print(h)