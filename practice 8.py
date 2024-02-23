#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1.Get the characters from the string
user_input = input("Enter a string: ")
print("Characters in the string:")
for char in user_input:
    print(char)


# In[17]:


# 2.Return the length of a string
user_input = input("Enter a string: ")
length_of_string = len(user_input)
print("Length of the string:", length_of_string)


# In[ ]:


# 3.Convert string into upper case
user_input = input("Enter a string: ")
uppercase_string = user_input.upper()
print("Uppercase string:", uppercase_string)


# In[ ]:


# 4.Split the string into sub-strings
user_input = input("Enter a string: ")
sub = user_input.split()
print("Substrings:",sub)


# In[5]:


# 5.Make a simple calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except :
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")


# In[19]:


# 6. Change the value of the list item
my_list = [1, 2, 3, 4, 5]
print("Original List:",my_list)
my_list[2] = 10
print("Modified List:",my_list)


# In[ ]:


# 7. Loop through a list
didnt understtood the question


# In[4]:


# 8.Length of a list
user_list = input("Enter elements of the list separated by space: ").split()
user_list = [int(item) for item in user_list]
list_length = len(user_list)
print("Length of the list : ",list_length)


# In[9]:


# 9.Add an item to a specified index
original_string = input("Enter a string: ")
item_to_add = input("Enter the item to add: ")
position = int(input("Enter the position to add the item: "))
string_list = list(original_string)
string_list.insert(position, item_to_add)
modified_string = ''.join(string_list)
print("Modified String:", modified_string)


# In[ ]:


# 10.Remove an item from a specified index
original_string = input("Enter a string: ")
item_to_remove = input("Enter the item to remove: ")
modified_string = original_string.replace(item_to_remove, '')
print("Modified String:", modified_string)

