#!/usr/bin/env python
# coding: utf-8

# ## Numpy

# ### Create an array

# In[1]:


import numpy as np


# In[2]:


x = [1,2,3,4]
np.array(x)


# In[3]:


y = [1,2,3],[4,5,6],[7,8,9]
np.array(y)


# In[4]:


np.arange(10,25)


# In[5]:


np.arange(10,100,5)


# In[6]:


np.zeros(5)


# In[7]:


np.zeros(5, dtype=int)


# In[8]:


np.ones(7)


# In[9]:


np.ones(7,dtype=int)


# In[10]:


np.ones((2,5))


# In[11]:


np.linspace(1,2,5)


# In[12]:


np.eye(5)


# In[13]:


np.random.rand(2,4)


# In[14]:


np.random.randn(2,4)


# In[15]:


np.random.randint(1,5,3)


# In[16]:


x = np.arange(2,10)
x


# In[18]:


y = np.random.randint(1,5,6)
y


# In[19]:


x.min()


# In[20]:


x.max()


# In[21]:


x.argmin()


# In[22]:


y.argmin()


# In[23]:


x.argmax()


# In[24]:


y.argmax()


# In[26]:


x.dtype


# In[28]:


a = np.eye(5)
a


# In[29]:


a = np.random.rand(2,3)
a


# In[30]:


a.T


# In[31]:


abc = np.arange(10,100,5)
abc


# In[33]:


abc = abc.reshape(6,3)
abc


# In[35]:


abc[4] = 100
abc


# In[36]:


xyz = np.arange(5,20)
xyz


# In[37]:


xyz[2:7]


# In[39]:


xyz[1:4] = 10
xyz


# ### Two Dimensional array

# In[40]:


import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a


# In[41]:


a[2][2]


# In[42]:


a[1][2]


# In[43]:


a[:,2]


# In[44]:


a[2,2]


# In[45]:


a [0:2,1:2]


# In[46]:


a[1:,2:]


# In[47]:


a[2]


# In[48]:


b = np.arange(2,20)
b


# In[49]:


b + b


# In[50]:


np.exp(b)


# In[52]:


b


# In[53]:


np.sqrt(b)


# In[54]:


np.log(b)


# In[55]:


np.max(b)


# In[56]:


np.min(b)


# In[57]:


np.argmax(b)


# In[58]:


np.argmin(b)


# In[59]:


np.var(b)


# In[60]:


np.std(b)


# In[61]:


np.mean(b)


# In[62]:


np.median(b)


# In[63]:


np.square(b)


# In[64]:


xy = np.random.rand(3,4)
xy


# In[70]:


np.round(xy,decimals=3)


# In[71]:


fruits = np.array(["apple","apple","mango","banana"])
np.unique(fruits)


# In[ ]:




