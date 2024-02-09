#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Higher order function

def add(x):
    return x+1
def multiply(x):
    return x*2
def apply(func,x):
    return func(x)
print(apply(multiply,3))


# In[4]:


#  Lambda function

add=lambda x:x+1
multiply=lambda x:x*3
print(add(3))


# In[3]:


# map(),filter() and reduce()
data = [1, 2, 3, 4, 5]
result1 = map(lambda x: x * 2, data)
result2 = filter(lambda x: x % 2 == 0, data)
from functools import reduce
result3 = reduce(lambda x, y: x * y, data)


# In[44]:


# List comprehension using lambda  
data = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, data)
print(result)


# In[4]:


# Using 'IN'

data=[5,6,7,8,9]
result1=[x*3 for x in data]
print(result1)
result2=[x for x in data if x%3]
print(result2)


# In[5]:


# Use 'MAP' functions (15 exe)


# In[58]:


# Write a Python program to triple all numbers in a given list of integers.
nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))


# In[59]:


# Write a Python program to add three given lists using Python map
nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
print("Original list: ")
print(nums1)  
print(nums2)  
print(nums3)  
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3) 
print("\nNew list after adding above three lists:")
print(list(result))


# In[62]:


# Write a Python program to listify the list of given strings individually using Python map.
color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print("Original list: ")
print(color) 
print("\nAfter listify the list of strings are:") 
result = list(map(list, color)) 
print(result)


# In[63]:


# Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Base numbers abd index: ")
print(bases_num)
print(index)
result = list(map(pow, bases_num, index))
print("\nPower of said number in bases raised to the corresponding number in the index:")
print(result)


# In[64]:


# Write a Python program to square the elements of a list 
def square_num(n):
    return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))


# In[65]:


# Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence.
def change_cases(s):
    return str(s).upper(), str(s).lower()
 
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))


# In[66]:


# Write a Python program to add two given lists and find the difference between them.
def addition_subtrction(x, y):
    return x + y, x - y
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print("Original lists:")
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print("\nResult:")
print(list(result))


# In[67]:


# Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
nums_list = [1,2,3,4]
nums_tuple = (0, 1, 2, 3) 
print("Original list and tuple:")
print(nums_list)
print(nums_tuple)
result_list = list(map(str,nums_list))
result_tuple = tuple(map(str,nums_tuple))
print("\nList of strings:")
print(result_list)
print("\nTuple of strings:")
print(result_tuple)


# In[68]:


#  Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
print("Original data:")
print(student_data)
students_data_name = list(map(lambda x:x[0], student_data))
students_data_dob = list(map(lambda x:x[1], student_data))
students_data_weight = list(map(lambda x:int(x[2][:-2]), student_data))
print("\nStudent name:")
print(students_data_name)
print("Student name:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)


# In[69]:


# Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers.
import itertools
n = 10
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y
print("First 10 Fibonacci numbers:")
result = list(itertools.islice(fibonacci_nums(), n))
print(result)
square = lambda x: x * x 
print("\nAfter squaring said numbers of the list:")
print(list(map(square, result)))


# In[70]:


# Write a Python program to compute the sum of elements of an array of integers.
from array import array
def array_sum(nums_arr):
    sum_n = 0
    for n in nums_arr:
        sum_n += n
    return sum_n

nums = array('i', [1, 2, 3, 4, 5, -15])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = array_sum(nums_arr)
print("Sum of all elements of the said array:")
print(result)


# In[71]:


# Write a Python program to count the same pair in two given lists
from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result

nums1 = [1,2,3,4,5,6,7,8]
nums2 = [2,2,3,1,2,6,7,9]
print("Original lists:")
print(nums1)
print(nums2)
print("\nNumber of same pair of the said two given lists:")
print(count_same_pair(nums1, nums2))


# In[72]:


# Write a Python program to interleave two lists into another list randomly. Use the map() function.
import random
def randomly_interleave(nums1, nums2):
    result =  list(map(next, random.sample([iter(nums1)]*len(nums1) + [iter(nums2)]*len(nums2), len(nums1)+len(nums2))))
    return result
nums1 = [1,2,7,8,3,7]
nums2 = [4,3,8,9,4,3,8,9]
print("Original lists:") 
print(nums1)
print(nums2)
print("\nInterleave two given list into another list randomly:")
print(randomly_interleave(nums1, nums2))


# In[73]:


# Write a Python program to split a given dictionary of lists into list of dictionaries using the map function.
def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))


# In[74]:


# Write a Python program to convert a given list of strings into a list of lists using the map function.
def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)

colors = ["Red", "Green", "Black", "Orange"]
print('Original list of strings:')
print(colors)
print("\nConvert the said list of strings into list of lists:")
print(strings_to_listOflists(colors))


# In[6]:


# Use 'FILTER' functions (15 exe)


# In[21]:


#Filter even numbers from a list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)


# In[22]:


# Filter words longer than 5 characters from a list of strings:
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
filtered = list(filter(lambda word: len(word) > 5, words))
print(filtered)


# In[23]:


# Filter positive numbers from a list:
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x > 0, numbers))
print(filtered)


# In[24]:


# Filter prime numbers from a list:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
filtered = list(filter(is_prime, numbers))
print(filtered)


# In[25]:


# Filter non-empty strings from a list:

strings = ["apple", "", "banana", "", "cherry", "date", ""]
filtered = list(filter(lambda s: len(s) > 0, strings))
print(filtered)


# In[26]:


# Filter even-length strings from a list of strings:

strings = ["apple", "banana", "cherry", "date", "fig", "grape"]
filtered = list(filter(lambda s: len(s) % 2 == 0, strings))
print(filtered)


# In[27]:


# Filter elements that are not None from a list:

elements = [1, None, "hello", None, 42, None, 3.14]
filtered = list(filter(lambda x: x is not None, elements))
print(filtered)


# In[ ]:


# Filter dictionaries with a specific key:
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "score": 90}, {"name": "Charlie"}]
filtered = list(filter(lambda d: "age" in d, data))
print(filtered)


# In[28]:


# Filter elements based on their data type:
elements = [1, "hello", 3.14, [1, 2, 3], (4, 5), {"name": "John"}]
filtered = list(filter(lambda x: isinstance(x, int), elements))
print(filtered)


# In[10]:


# Filter names that start with a specific letter in a list:

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
start_letter = "C"
filtered = list(filter(lambda name: name.startswith(start_letter), names))
print(filtered)


# In[11]:


# Filter numbers greater than a specific threshold:

numbers = [12, 34, 56, 78, 90, 45, 23, 67]
threshold = 50
filtered = list(filter(lambda x: x > threshold, numbers))
print(filtered)


# In[ ]:


# Filter elements containing a specific substring in a list of strings:

strings = ["apple", "banana", "cherry", "date", "fig", "grape"]
substring = "an"
filtered = list(filter(lambda s: substring in s, strings))
print(filtered)


# In[ ]:


# Filter elements based on a custom function:

def custom_filter_function(item):
    return 
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered = list(filter(custom_filter_function, elements))
print(filtered)


# In[18]:


# Filter elements based on a lambda function with multiple conditions:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda x: x % 2 == 0 and x > 5, numbers))
print(filtered)


# In[ ]:


# use 'reduce' function (15 exe)


# In[20]:


# Calculate the sum of all elements in a list:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)


# In[29]:


# Find the product of all elements in a list:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)


# In[32]:


# Calculate the factorial of a number:
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)


# In[33]:


# Find the maximum element in a list:
numbers = [43, 67, 12, 89, 54]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)


# In[34]:


# Find the minimum element in a list:
numbers = [43, 67, 12, 89, 54]
min_value = reduce(lambda x, y: x if x < y else y, numbers)
print(min_value)


# In[35]:


# Concatenate a list of strings:
strings = ["Hello", " ", "World", "!"]
concatenated = reduce(lambda x, y: x + y, strings)
print(concatenated)


# In[36]:


# Join a list of words into a sentence:
words = ["This", "is", "a", "sentence."]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)


# In[37]:


# Combine a list of dictionaries into one dictionary:
data = [{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"d": 5}]
combined = reduce(lambda x, y: {**x, **y}, data)
print(combined)


# In[38]:


# Calculate the cumulative sum of elements in a list:
numbers = [1, 2, 3, 4, 5]
cumulative_sums = reduce(lambda x, y: x + [x[-1] + y], numbers, [0])[1:]
print(cumulative_sums)


# In[39]:


# Find the longest word in a list of strings:
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest_word)


# In[41]:


# Count the number of occurrences of a specific element in a list:
from functools import reduce
numbers = [1, 2, 2, 3, 2, 4, 2, 5]
count = reduce(lambda x, y: x + (1 if y == 2 else 0), numbers, 0)
print(count)


# In[ ]:


# Calculate the power of 2 raised to the sum of elements in a list:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
power = reduce(lambda x, y: 2 ** (x + y), numbers)
print(power)


# In[ ]:


# Find the greatest common divisor (GCD) of a list of numbers:
from functoola import reduce
import math
numbers = [24, 36, 48, 60]
gcd = reduce(math.gcd, numbers)
print(gcd)


# In[ ]:


# Calculate the running average of a list of numbers:
numbers = [1, 2, 3, 4, 5]
averages = [reduce(lambda x, y: (x[0] + y, x[1] + 1), numbers[:i+1], (0, 0))[0] / (i+1) for i in range(len(numbers))]
print(averages)


# In[ ]:


# Merge a list of lists into a single list:
lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
merged = reduce(lambda x, y: x + y, lists)
print(merged)


# In[ ]:


# Find the largest of given numbers

from functools import reduce
num = [20,22,24,12,6,88,10,55,66]    
def large(x, y):  
    return x if x > y else y   
largest = reduce(large, num)  
print(f"Largest found with method 1: {largest}")  


# In[ ]:


# Find the largest of given numbers (one liner)
largest = reduce(lambda x,y: x if x > y else y, num)  
print(f"Largest found with method 2: {largest}")  


# In[ ]:


# Pass Statement

seq = {"Python","Pass","Statement","Placeholder"}  
for value in sequ:  
    if value == "Pass":  
        pass 
    else:  
        print("Not reached pass keyword: ", value)  


# # Tuple 

# In[11]:


# Create an empty tuple

empty_tuple=()
print(empty_tuple)


# In[12]:


# Create tuple having integers

int_tuple=(55,66,44,88,33)
print(int_tuple)


# In[13]:


# Create tuple having objects of different data types

mixed_tuple=(58,'AIDTM',6.89)
print(mixed_tuple)


# In[14]:


# Create a nested tuple

nested_tuple=(59,{4:5,8:6,'a':8},{1,2,3},(5,8,6,0))
print(nested_tuple)


# In[15]:


# How to access element in tuple

tuple_=('Finance','Marketing','Python','Data_analytics')
print(tuple_[2])
try:
    print(tuple_[5])
except Exception as e:
    print(e)


# In[16]:


# Access elements through index of floating number
try:
    print(tuple_[1.0])
except Exception as e:
    print(e)


# In[17]:


# Creating a nested tuple

nested_tuple=('Tuple',[1,2,3,5,6],(5,8,6,4,2))
print(nested_tuple[0][3])
print(nested_tuple[1][1])


# In[18]:


# Negative indexing in tuple

tuple_1=('Python','PowerBI','Excel','Collection')
print('Element at -1 index: ',tuple_1[-1])
print(tuple_1[-4:-1])


# In[19]:


# Slicing in python tuple

tuple_1=('Python','PowerBI','Excel','Collection')
print(tuple_1[1:3])
print(tuple_1[:-2])
print(tuple_1[:])


# In[20]:


# Delete an element

tuple_1=('Python','PowerBI','Excel','Collection')
try:
    del tuple_1[3]
    print(tuple_1)
except Exception as e:
    print(e)


# In[21]:


del tuple_1
tuple_1=('Python','PowerBI','Excel','Collection')
try:
    print(tuple_1)
except Exception as e:
    print(e)


# In[22]:


# Repetition in python

tuple_1=('Python','PowerBI','Excel','Collection')
print('Original tuple is: ',tuple_1)
tuple_1=tuple_1*3
print('New tuple is: ',tuple_1)


# In[23]:


# Counting appearance in tuple

t1=(0,1,2,3,4,5,6,7,5,9,4,1,2)
t2=('python','finance','python','java','excel','java')
res=t1.count(2)
res1=t2.count('java')
print(res,res1)


# In[24]:


# Getting index of a number

tuple_data=(0,1,2,3,4,5,6,3,4,88,9)
res=tuple_data.index(3)
res1=tuple_data.index(3,4)
print(res)
print(res1)


# In[25]:


# Membership test

Tuple=('Python','Tuple','Ordered','Immutable','Collection','Ordered')
print('Tuple' in Tuple)
print('Items' in Tuple)
print('Immutable' not in Tuple)
print('Items' not in Tuple)


# In[26]:


# Iterate over tuple elements

Tuple=('Python','Tuple','Ordered','Immutable','Collection','Ordered')
for item in Tuple:
    print(item)


# In[27]:


# Concatenate tuples 

Tuple=('Python','Tuple','Ordered','Immutable','Collection','Ordered')
print(Tuple+(4,5,6))


# In[28]:


# Set

days=set(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
print(days)
print(type(days))
print('Looping through the set elements: ')
for i in days:
    print(i)
set3={}
print(type(set3))
set4=set()
print(type(set4))


# In[29]:


# add element in set
Months=set(['January','February','March','April','May','June'])
print("\nprinting the original set...")
print(Months)
print("\nAdding other months to set...")
Months.add("July")
Months.add("August")
print("\nPrinting the modified set...")
print(Months)
print("\nlooping through the set elements...")
for i in Months:
    print(i)


# In[30]:


# update element in set
Months=set(['January','February','March','April','May','June'])
print("\nprinting the Original set...")
print(Months)
print("\nupdating the original set...")
Months.update(['July','August','September','October'])
print("\nprinting the modified set...")
print(Months)


# In[31]:


# discard element from set
Months=set(['January','February','March','April','May','June'])
Months.discard("January")
print(Months)


# In[32]:


# remove 
Months=set(['January','February','March','April','May','June'])
Months.remove("March")
print(Months)


# In[33]:


# pop
Months=set(['January','February','March','April','May','June'])
Months.pop()
print(Months)


# In[34]:


# clear
Months=set(['January','February','March','April','May','June'])
Months.clear()
print(Months)


# In[35]:


# Union of sets with 2 methods

days1={'Monday','Tuesday','Wednesday','Thursday','Sunday'}
days2={'Friday','Saturday','Sunday'}
print(days1|days2)


# In[36]:


days1={'Monday','Tuesday','Wednesday','Thursday','Sunday'}
days2={'Friday','Saturday','Sunday'}
print(days1.union(days2))


# In[37]:


# Intersection of sets with 2 methods

days1={'Monday','Tuesday','Wednesday','Thursday','Sunday'}
days2={'Friday','Saturday','Sunday'}
print(days1&days2)


# In[38]:


days1={'Monday','Tuesday','Wednesday','Thursday','Sunday'}
days2={'Friday','Saturday','Sunday'}
print(days1.intersection(days2))


# In[39]:


# Difference of sets with 2 methods

days1={'Monday','Tuesday','Wednesday','Thursday','Sunday'}
days2={'Friday','Saturday','Sunday'}
print(days1-days2)


# In[40]:


days1={'Monday','Tuesday','Wednesday','Thursday','Sunday'}
days2={'Friday','Saturday','Sunday'}
print(days1.difference(days2))


# In[41]:


# Superset,Subset and Equivalent

days1={'Monday','Tuesday','Wednesday','Thursday'}
days2={'Monday','Tuesday'}
days3={'Monday','Tuesday','Friday'}
print(days1>days2)
print(days1<days2)
print(days2==days3)


# # NumPy

# In[42]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)


# In[43]:


print(np.__version__)


# In[44]:


print(type(arr))


# In[45]:


# Using tuple to create a NumPy array

import numpy as np
arr=np.array((1,2,3,4,5))
print(arr)


# In[31]:


# creating 0 D array using 

import numpy as np
arr = np.array(42)
print(arr)


# In[35]:


# creating 1 D array using

import numpy as np
arr = np.array([1,2,3])
print(arr)


# In[5]:


# creating 2 D array using 
import numpy as np
arr= np.array([[1,2,3],[4,5,6]])
print(arr)


# In[6]:


# creating 3 D array using 
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)


# In[7]:


# creating 5 D array using 
import numpy as np
arr=np.array([1,2,3],ndmin=5)
print(arr)
print(arr.ndim)


# In[8]:


# Get first element of array
import numpy as np
arr=np.array([1,2,3,4])
print(arr[0])
print(arr[2]+arr[3])


# In[9]:


# add element 
import numpy as np
arr=np.array([1,2,'Python',' is best'])
print(arr[2]+arr[3])


# In[10]:


import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1])
print(arr[1,3])


# In[11]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])


# In[12]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])
print(arr[::2])


# In[13]:


import numpy as np
arr=np.array(['apple','banana','chickoo'])
print(type(arr))


# In[14]:


import numpy as np
arr=np.array([1,2,3],dtype='S')
print(type(arr))

# some data types in mupoy

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type 
# In[15]:


# Data types in NumPy

import numpy as np 
arr=np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)
arr=np.array([1.1,2.6,3.1])
newarr=arr.astype(int)
print(newarr)
print(newarr.dtype)


# In[16]:


import numpy as np 
arr=np.array([1,2,3,4])
x=arr.copy()
arr[0]=42
print(arr)
print(x)


# In[17]:


import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)


# In[18]:


import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr[:, ::2]):
    print(x)    


# In[57]:


# Enumerate on 2D array's elements

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for idx,x in np.ndenumerate(arr):
    print(idx, x)


# In[56]:


#Join two arrays (conacte)

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2))
print(arr)


# In[21]:


# stacking
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr=np.stack((arr1,arr2),axis=1)
print(arr)


# In[22]:


# split array in 3 part

import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr)


# In[23]:


# access the splitted array

import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[24]:


# find value at given index
import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)


# In[25]:


import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8])
x1=np.where(arr1%2==0)
print(x1)


# In[26]:


# sort given array
import numpy as np
arr=np.array([3,2,0,1])
print(np.sort(arr))


# In[1]:


#Create a filter array that will return only values higher 

import numpy as np
arr=np.array([41,42,43,44])
filter_arr = []
for element in arr:   
    if element > 42:
        filter_arr.append(True) 
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# In[28]:


from numpy import random
x=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print(x)

