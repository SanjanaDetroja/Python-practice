#!/usr/bin/env python
# coding: utf-8

# In[3]:


# count number of vowels and consonents in string
string = input("enter the string: ")
vowels = 0
consonants = 0
for i in string:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
            vowels = vowels + 1;
    else:
        consonants = consonants + 1;
print("The number of vowels:",vowels);
print("The number of consonant:",consonants);


# In[6]:


# some random pattern
my_string = "sanjana"
x = 0
for i in my_string:
    x = x + 1
    print (my_string[0:x])
#print(" ") # for adding space in between sanjana and sanjan
for i in my_string:
    x = x - 1
    print (my_string[0:x])# we do different type by using -x and many for changes
    


# In[7]:


# PRINT sQUARE
n = 4
for i in range(n):
    for j in range(n):
        print('*' , end=' ')
    print()


# In[8]:


name = ("Sanjana")
n = 7
print("Tuple with a loop")
for i in range(int(n)):
    name = (name,)
print(name)


# In[10]:


# zipping
first_names = ('Sanjana', 'Sanjay', 'Mohit', 'jay')
last_names = ('detroja', 'detroja', 'bhoru', 'taplo')
ages = (22, 45, 22, 35)
zipped = zip(first_names, last_names,ages)
fullname = tuple(zipped)
print("fullname:",fullname)


# In[11]:


# join
myname = ("Sanjana", "Sanjaybhai", "Detroja")
x = "#".join(myname)
print(x)


# In[12]:


# translate ( works ascii table in which a-z/97-122 and A-Z/65-90)
mydict = {100:  68}#100 is d and 68 is D
txt = "Sanjana detroja"
print(txt.translate(mydict))


# In[13]:


# strip (remove starting and ending of string)
txt = ",.,.,.,abc Sanjana ...,,.,abc"
x = txt.strip(",.abc")
print(x)


# In[14]:


#rjust (we can fil extra space with any special character)
txt = "500"
print(txt.rjust(10, '$'))

#zfill (fill extra place)
txt = "5000"
x = txt.zfill(10)
print(x)


# #escape sequence

# In[15]:


txt = "I am Sanjana \"Detroja\" from the Gujarat."
print (txt)
#\'	Single Quote	(adding "" in string)

txt = "I am Sanjana \\Detroja\\ from the Gujarat."
print (txt)
#\\	Backslash	(adding \ in string)

txt = "I am Sanjana\nDetroja\nfrom the Gujarat."
print (txt)
#\n	New Line	(print in new line)

txt = "I am Sanjana Detroja from the Gujarat.\r123"
print (txt)
#\r	Carriage Return	(replace the element which is after \r will from first)

txt = "I am Sanjana\tDetroja from the Gujarat."
print (txt)
#\t	Tab	(add extra space)

txt = "I am Sanjana\bDetroja from the Gujarat."
print (txt)
#\b	Backspace	(will remove extra space)

txt = "I am Sanjana\fDetroja from the Gujarat."
print (txt)
#\f formfeed


# In[ ]:




