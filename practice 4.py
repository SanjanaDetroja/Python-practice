#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[7]:


#pip install pandas


# In[ ]:





# In[15]:


#1 create an empty series,by defaukt the data is float 64
import pandas as pd
x=pd.Series()
print(x)

import numpy as np
info = np.array(['P','a','n','d','s'])
a=pd.Series(info)
print(a)


# In[21]:


#2 accessing data in a series
import pandas as pd
x=pd.Series([1,2,3],index=['a','b','c'])
print(x[1])
print(x['a'])


# In[23]:


#3 we can retrieve index array and data array of an existing series object by using the attribute indesx and vlues
import pandas as pd
import numpy as np
x=pd.Series(data=[2,4,6,8])
y=pd.Series(data=[11.2,18.6,22.5],index=['a','b','c'])
print(x.index)
print(x.values)
print(y.index)
print(y.values)


# In[26]:


#4 shape of a series element i.e total elements including the missing and empty values (NaN)
import pandas as pd
import numpy as np
a=pd.Series(data=[1,2,3,4])
b=pd.Series(data=[3.4,6.5,8.2],index=['x','y','z'])
print(a.shape)
print(b.shape)


# In[43]:


#5 check the series object is empty or not,find length and count
import pandas as pd
import numpy as np
a=pd.Series(data=[1,2,3,np.NaN])
b=pd.Series(data=[3.4,6.5,8.2],index=['x','y','z'])
c=pd.Series()
print(a.empty,b.empty,c.empty)
print(a.hasnans,b.hasnans,c.hasnans)
print(len(a),len(b))
print(a.count(),b.count())


# In[28]:


#6 how to create an empty dataframe (how to import a dataframe)
import pandas as np
df=pd.DataFrame()
print(df)


# In[29]:


#7 create a dataframe
import pandas as pd
x=['python','java']
df=pd.DataFrame(x)
print(df)


# In[30]:


#8 creating data frame from dictionary of ndarrays/list
import pandas as pd
info={'ID':[101,121,103],'DEPARTMENT':['B.Sc','B.Tech','M.Tech']}
df=pd.DataFrame(info)
print(df)


# # COLUMN OPERATIONS

# In[37]:


#9 select the column
import pandas as pd
info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
      'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
d1=pd.DataFrame(info)
print(d1)
print(d1['one'])


# In[41]:


#10 program to add columns
import pandas as pd
info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
      'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
df=pd.DataFrame(info)
print("add new column by passing series")
df['three']=pd.Series([20,40,60],index=['a','b','c'])
print(df)
print("add new column using existing data frame column")
df["four"]=df["one"]+df["three"]
print(df)


# In[42]:


#11 delete one column
import pandas as pd
info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
      'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
    
df=pd.DataFrame(info)
print("the Data Frame")
print(df)
print("delete the first column")
del df['one']
print(df)
print("delete another column")
df.pop("two")
print(df)


# # raw operations

# In[45]:


#12 local function
import pandas as pd
info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
      'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
df=pd.DataFrame(info)
print(df.loc['b'])


# In[47]:


#13 slicing the raw
info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
      'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
df=pd.DataFrame(info)
print(df[1:5])


# 

# In[48]:


#14 add one raw
d=pd.DataFrame([[7,8],[9,10]],columns=['x','y'])
d2=pd.DataFrame([[12,10],[11,9]],columns=['x','y'])
d=d.append(d2)
print(d)


# In[55]:


#15 Deletion of raw
a_info=pd.DataFrame([[4,5],[6,7]],columns=['x','y'])
b_info=pd.DataFrame([[12,10],[11,9]],columns=['x','y'])
a_info=a_info.append(b_info)
a_info=a_info.drop(0)
print(a_info)


# In[57]:


#16 creating data set (proper indexing without repetition)
info1=pd.DataFrame({"x":[23,10,25,12],"y":[41,40,21,12]})
info2=pd.DataFrame({"x":[23,10,25],"y":[41,40,12],"z":[31,12,45]})
info1.append(info2,ignore_index=1)


# # MATPLOTLIB

# In[60]:


#17 GENERATING A SIMPLE GRAPH
from matplotlib import pyplot as plt
plt.plot([-1,2,3],[0,5,1])
plt.show()


# In[64]:


#18 adding name and title
x=[5,2,7]
y=[1,10,4]
plt.plot(x,y)
plt.title("Line Graph")
plt.ylabel("Y Axis")
plt.xlabel("X Axis")
plt.show()


# In[67]:


#19 ploting with colours
plt.plot([1,2,3,4,5],[1,4,9,16,25],'ro')
plt.axis([0,6,0,20])
plt.show()


# In[72]:


#20 categorical variables directly to many plotting funtions
names=['Ab','Cd','Ef']
marks=[87,50,98]
plt.figure(figsize=(9,3))
plt.subplot(133)
plt.bar(names,marks)
plt.subplot(132)
plt.scatter(names,marks)
plt.subplot(131)
plt.plot(names,marks)
plt.suptitle("categorical Plotting")
plt.show()


# In[73]:


#21  plotting graph and grid
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[16,8,10]
y=[8,10,6]
x2=[8,15,11]
y2=[6,15,7]
plt.plot(x,y,'r',label='line one',linewidth=5)
plt.plot(x2,y2,'m',label='line two',linewidth=5)
plt.title('Epic Info')
fig = plt.figure()
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.legend()
plt.grid(True,color='k')
plt.show()


# In[78]:


#22 plotting sine wave
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,100)
ax.plot(x,np.sin(x))


# In[85]:


#23 
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,100)
ax.plot(x,np.sin(x))
x=np.arange(0.0,2,0.01)
y1=np.sin(2*np.pi*x)
y2=1.2*np.sin(4*np.pi*x)
fig,ax = plt.subplots(1,sharex=True)
ax.plot(x,y1,x,y2,color='black')
ax.fill_between(x,y1,y2,where=y2>=y1,facecolor='orange',interpolate=True)
ax.fill_between(x,y1,y2,where=y2<=y1,facecolor='yellow',interpolate=True)
ax.set_title('fill between where')


# In[91]:


#24
from matplotlib import pyplot as plt
players=['virat','rohit','hardik']
runs=[51,87,67]
plt.barh(players,runs,color='lightpink')
plt.title('Score Card')
plt.xlabel('players')
plt.ylabel('runs')
plt.show()


# In[93]:


#25
from matplotlib import pyplot as plt
from matplotlib import style
x=[5,8,7]
y=[12,16,8]
x2=[8,9,7]
y2=[7,15,7]
plt.bar(x,y,color='y',align='center')
plt.bar(x2,y2,color='c',align='center')
plt.title('information')
plt.ylabel('y axis')
plt.xlabel('x axis')


# In[95]:


#26
plt.style.use('fivethirtyeight')
mu=50
sigma=7
x=np.random.normal(mu,sigma,size=200)
fig,ax=plt.subplots()
ax.hist(x,20)
ax.set_title('histogram')
ax.set_xlabel('bin range')
ax.set_ylabel('frequency')
fig.tight_layout()
plt.show()


# In[100]:


#27 3 D plot
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
height=np.array([100,110,87,65,80,96,75,42,59,54])
weight=np.array([105,123,84,60,80,96,75,40,69,54])
plt.scatter(height,weight)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(height,weight)
plt.title("3d scatter plot")
plt.xlabel("height")
plt.ylabel("weight")
plt.title("3d scatter plot")
plt.xlabel("height")
plt.ylabel("weight")
plt.show


# In[ ]:




