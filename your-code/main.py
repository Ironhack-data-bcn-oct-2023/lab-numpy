#1. Import the NUMPY package under the name np.
print("\n1. Import the NUMPY package under the name np.\n" + "-"*50+"\n")
print("See coding..")

import numpy as np

#2. Print the NUMPY version and the configuration.
print("\n2. Print the NUMPY version and the configuration\n" + "-"*50+"\n")

print("Version: " + np. __version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
print("\n3. 3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable a\n" + "-"*50+"\n")
print("See coding..")

a =  np.random.rand(2,3,5)

#4. Print a.
print("\n4. Print a.\n" + "-"*50+"\n")
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
print("\n5.Create a 5x2x3 3-dimensional array with all values equaling 1...\n" + "-"*50+"\n")
print("See code...")
b = np.ones((5,2,3), dtype=int)

#6. Print b.
print("\n6. Print b.\n" + "-"*50+"\n")

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?
print("\n7. Do a and b have the same size? How do you prove that in Python code?.\n" + "-"*50+"\n")

print("Yes, they have same size. We compare them True is returned\n")
print(a.size == b.size)

#8. Are you able to add a and b? Why or why not?
print("\n8. Are you able to add a and b? Why or why not?.\n" + "-"*50+"\n")

'''Arrays can be add only if they have same shape. Otherwise you'll have an error.'''


print("Arrays can be add only if they have same shape. Otherwise you'll have an error.")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
print("\n9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable.\n" + "-"*50+"\n")

print(a.shape)
print(b.shape)
c = b.transpose(1,2,0)
print(a.shape == c.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
print("\n10. Try to add a and c. Now it should work. Assign the sum to variable ''d''. But why does it work now?\n" + "-"*50+"\n")

'''
Now will work because after transpose() action , both array shapes are equal.
'''

d = a+c
print(d)
print('Now will work because after transpose() action , both array shapes are equal.')

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("\n11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.\n" + "-"*50+"\n")

print(a)
print(d)

print("All values of arrays have been increased in 1. That's because we add an array generated with ones()\n")

#12. Multiply a and c. Assign the result to e.
print("\n12. Multiply a and c. Assign the result to e.\n" + "-"*50+"\n")

e =  a * c
print(e)

#13. Does e equal to a? Why or why not?
print("\n13. Does e equal to a? Why or why not?\n" + "-"*50+"\n")

print("e is equal to a?: YES")
print("because we multiplied a by 1 (c array are ones)")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print("\n14. Identify the max, min, and mean values in d. Assign those values to variables d_max, d_min, and d_mean\n" + "-"*50+"\n")

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

print(f"Max: {d_max}")
print(f"Min: {d_min}")
print(f"Mean: {d_mean}")



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
print("\n15. Now we want to label the values in d. First create an empty array f with the same shape (i.e. 2x3x5) as d using `np.empty`.\n" + "-"*50+"\n")

f = np.empty((2,3,5),dtype=int)
print(f.size)
print(f.shape)
print(f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

print("\n16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than.....\n" + "-"*50+"\n")


l1=0
l2=0
l3=0

for i in d:
        for y in i:
                for z in y:
                        if z > d_min and z < d_mean:
                                f[l1][l2][l3] = 25
                        if z > d_mean and z < d_max:
                                f[l1][l2][l3] = 75
                        if  z == d.mean:
                                f[l1][l2][l3] = 50
                        if z == d_min:
                                f[l1][l2][l3] = 0
                        if z == d_max:
                                f[l1][l2][l3] = 100
                        l3+=1
                l2+=1
                l3=0
        l1+=1
        l2=0
        
                        
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

print("\n17.Print d and f. Do you have your expected f?.....\n" + "-"*50+"\n")

print(d)
print("."*50)
print(f)

print("\nYES: f HAS EXPECTED VALUES COMING FROM COMPARISON OF d WITH d_ min,d_max,d_mean\n")

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


print("\n18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values .....\n" + "-"*50+"\n")

f_string = np.empty((2,3,5),dtype=str)

l1=0
l2=0
l3=0

for i in d:
        for y in i:
                for z in y:
                        if z > d_min and z < d_mean:
                                f_string[l1][l2][l3] = "B"
                        if z > d_mean and z < d_max:
                                f_string[l1][l2][l3] = "D"
                        if  z == d.mean:
                                f_string[l1][l2][l3] = "C"
                        if z == d_min:
                                f_string[l1][l2][l3] = "A"
                        if z == d_max:
                                f_string[l1][l2][l3] = "E"
                        l3+=1
                l2+=1
                l3=0
        l1+=1
        l2=0
        
                        
print(f_string)

