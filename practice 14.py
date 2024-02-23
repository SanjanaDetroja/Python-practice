#!/usr/bin/env python
# coding: utf-8

# In[4]:


import plotly.express as px 
# using the tips dataset 
df = px.data.tips() 
# plotting the violin chart 
fig = px.violin(df, x="day", y="total_bill") 
# showing the plot 
fig.show()


# In[3]:


import plotly.figure_factory as ff 
# Data to be plotted 
df = [dict(Task="A", Start='2020-01-01', Finish='2009-02-02'), 
    dict(Task="Job B", Start='2020-03-01', Finish='2020-11-11'), 
    dict(Task="Job C", Start='2020-08-06', Finish='2020-09-21')] 
# Creating the plot 
fig = ff.create_gantt(df) 
fig.show()


# In[1]:


import plotly.graph_objects as go 
import numpy as np 
# Data to be plotted 
x = np.outer(np.linspace(-2, 2, 30), np.ones(30)) 
y = x.copy().T 
z = np.cos(x ** 2 + y ** 2) 
# plotting the figure 
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)]) 
fig.show()


# In[5]:


from scipy import constants

print(constants.minute)
print(constants.hour)
print(constants.day)
print(constants.week)
print(constants.year)
print(constants.Julian_year)


# In[6]:


from scipy import constants

print(constants.inch)
print(constants.foot)
print(constants.yard)
print(constants.mile)
print(constants.mil)
print(constants.pt)
print(constants.point)
print(constants.survey_foot)
print(constants.survey_mile)
print(constants.nautical_mile)
print(constants.fermi)
print(constants.angstrom)
print(constants.micron)
print(constants.au)
print(constants.astronomical_unit)
print(constants.light_year)
print(constants.parsec)


# In[7]:


import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))


# In[8]:


import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))


# In[9]:


from scipy.optimize import root
from math import cos
def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)


# In[13]:


import plotly.express as px
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()


# In[14]:


import plotly.express as px
df = px.data.tips()
fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='day')
fig.show()


# In[ ]:




