#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1 Get the characters from the string
strr = input("Enter a string: ")

print("Characters in the string: ")
for char in strr:
    print(char)


# In[7]:


# 2 Return the length of a string
strr = input("Enter a string: ")
lenstrr = len(strr)
print("Length of the string:", lenstrr)


# In[8]:


# 3 Convert string into upper case
strr = input("Enter a string: ")
print(strr.upper())


# In[9]:


# 4 Split the string into sub-strings
strr = input("Enter a string: ")
print(strr.split())


# In[11]:


# 5 Make a simple calculator
print("select the operation you want\n"\
            "1.addition\n"\
            "2.subtraction\n"\
            "3.multiplication\n"\
            "4.division\n")
option=int(input("enter any value from '1','2','3','4'"))
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
if option==1:
    s=num1+num2
    print("the sum is: ",s)
elif option==2:
    sub=num1-num2
    print("the difference is: ",sub)
elif option==3:
    mul=num1*num2
    print("the product is: ",mul)
elif option==4:
    div=num1/num2
    print("the division product is: ",div)


# In[12]:


# 6 Change the value of the list item
my_list = [1, 2, 3, 4, 5]
print("Original List:",my_list)
my_list[0] = 6
print("Modified List:",my_list)


# In[20]:


# 7 Loop through a list
list1=[1, 2, 3, 4, 5]
i=0
for i in list1:
    print(i)


# In[13]:


# 8 Length of a list
user_list = input("Enter elements of the list separated by space: ").split()
user_list = [int(item) for item in user_list]
list_length = len(user_list)
print("Length of the list : ",list_length)


# In[15]:


# 9 Add an item to a specified index
strr1 = input("Enter a string: ")
nww = input("Enter the item to add: ")
position = int(input("Enter the position to add the item: "))
string_list = list(strr1)
string_list.insert(position, nww)
modified_string = ''.join(string_list)
print("Modified String:", modified_string)


# In[17]:


# 10 Remove an item from a specified index
strr1= input("Enter a string: ")
item_to_remove = input("Enter the item to remove: ")
modified_string = strr1.replace(item_to_remove, '')
print("Modified String:", modified_string)


# In[ ]:




