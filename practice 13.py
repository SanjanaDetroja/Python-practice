# 1. Write a Pandas program to capitalize all the string values of specified columns of a given DataFrame.

import pandas as pd
df = pd.DataFrame({
    'name': ['alberto','gino','ryan', 'Eesha', 'syed'],
    'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)
print("\nAfter capitalizing name column:")
df['name'] = list(map(lambda x: x.capitalize(), df['name']))
print(df)


# 2. Write a program for Ranking Rows of Pandas DataFrame

import pandas as pd 
movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'], 
		'Year': ['1972', '2018', '1999'], 
		'Rating': ['9.2', '6.8', '8.8']} 
df = pd.DataFrame(movies) 
print(df) 
df['Rating_Rank'] = df['Rating'].rank(ascending = 1)  
df = df.set_index('Rating_Rank') 
print(df) 
df = df.sort_index() 
print(df) 


# 3. Write a NumPy program to create a 3x3 identity matrix and stack it vertically and horizontally.

import numpy as np
# creating a 3x3 identity matrix
matrix = np.identity(3)
print("3x3 identity matrix:")
print(matrix)
# stacking the matrix vertically
vert_stack = np.vstack((matrix, matrix, matrix))
# stacking the matrix horizontally
horz_stack = np.hstack((matrix, matrix, matrix))
print("Vertical Stack:\n", vert_stack)
print("Horizontal Stack:\n", horz_stack)


# 4. Write a NumPy program to create a 5x5 array with random values and replace the minimum value with 0.

import numpy as np
# Create a 5x5 array with random values
nums = np.random.rand(5, 5)
print("Original array elements:")
print(nums)
# Find the minimum value in the array
min_val = nums.min()
# Replace the minimum value with 0
nums[nums == min_val] = 0
# Print the updated array
print("\nSaid array after replacing the minimum value with 0:")
print(nums)


# 5. Write a NumPy program to find the dot product of two arrays of different dimensions

import numpy as np
# Define the two arrays
nums1 = np.array([[1, 2], [3, 4], [5, 6]])
nums2 = np.array([7, 8])
print("Original arrays:")
print(nums1)
print(nums2)
# Find the dot product
result = np.dot(nums1, nums2)
# Print the result
print("Dot product of the said two arrays:")
print(result)


# 6. Write a program to change the font size of the x and y labels.
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8, 4))

x = ['Arjun', 'Bharath', 'Raju', 'Seeta', 'Ram']
y = [5, 7, 8, 4, 6]

plt.bar(x, y, color = 'g')

plt.xlabel('Students', fontsize = 18)
plt.ylabel('Marks', fontsize = 18)

#Default fontsize of text using legend
plt.legend(['Marks scored'])

plt.show()


# 7. Write a NumPy program to compute the histogram of nums against the bins.

import numpy as np
import matplotlib.pyplot as plt
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("nums: ",nums)
print("bins: ",bins)
print("Result:", np.histogram(nums, bins))
plt.hist(nums, bins=bins)
plt.show()


# 8. Write a Pandas program to calculate the mean of all students' scores. Data is stored in a dataframe.

import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("\nMean score for each different student in data frame:")
print(df['score'].mean())



# 8. Write a Pandas program to compare the elements of the two Pandas Series.

import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)



#9. Write a Pandas program to randomly select rows from Pandas DataFrame 

import pandas as pd

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
		'Age':[27, 24, 22, 32, 15],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']}

df = pd.DataFrame(data)
df.sample()


# 10.  Write a pandas program to Split a text column into two columns

import pandas as pd 

df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior', 'Jonny_Depp'], 
					'Age':[32, 34, 36]}) 

print("Given Dataframe is :\n",df) 

print("\nSplitting Name column into two different columns :") 
print(df.Name.apply(lambda x: pd.Series(str(x).split("_")))) 
# import Pandas as pd 
import pandas as pd 

# create a new data frame 
df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior', 'Jonny_Depp'], 
					'Age':[32, 34, 36]}) 

print("Given Dataframe is :\n",df) 

print("\nSplitting Name column into two different columns :") 

df[['First','Last']] = df.Name.apply( 
lambda x: pd.Series(str(x).split("_"))) 

print(df) 

