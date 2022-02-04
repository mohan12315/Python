#!/usr/bin/env python
# coding: utf-8

# ### Data types

# In[1]:


x = "Hello"
type(x)


# In[2]:


y = 5.2
type(y)


# In[3]:


z = 3
type(z)


# In[4]:


a = 1+2j
type(a)


# In[6]:


b =False
type(b)


# In[7]:


m = "True"
type(m)


# ### Rules for naming variable

# In[ ]:


### variable name should not start with number
### case sensitive
### variable does not allow special characters other than underscore


# In[1]:


1apple= "apple"
1apple


# In[2]:


a = "apple"
A


# In[3]:


-a = "apple"
-a


# In[4]:


_a = "apple"
_a


# In[5]:


first_name = "mohan"
first_name


# ### Lists

# In[8]:


a = [1,2,3,5.6,"apple",1+2j]
type(a)


# In[9]:


a[0]


# In[10]:


a[5]


# In[11]:


a[1]="Hi"


# In[12]:


print(a)


# In[15]:


a.reverse()
a


# ### Tuple

# In[18]:


b = (1,2,3,4.5,"hi",2+3j)
type(b)


# In[19]:


b.reverse()
b


# In[20]:


b= 1,2,3,4.5,"hi",2+3j
b


# ### Set

# In[ ]:


### Add heterogenous
### Does not allow duplicates
### cannot access using index
### immutable using index but its mutable


# In[9]:


sample_set = {1,2,123,5,4,8,9,1,2,3}
sample_set


# In[10]:


sample_set[2]


# In[11]:


sample_set[2]=100
sample_set


# In[13]:


sample_set.add(125)
sample_set


# ### Dictionary

# In[14]:


### dictionary has key value pair datastructure
### key is unique and values can be duplicated
### can retrieve the value using key
### can change the value using key
### key is immutable


# In[16]:


a_1 = {1:"apple",2:"mango",3:"banana",4:"apple"}
a_1


# In[17]:


a_1[2]="gauva"
a_1


# In[18]:


a_1[3]


# In[19]:


a_1["apple"]


# In[21]:


a_1[5]="mango"
a_1


# In[22]:


type(a_1)


# In[ ]:




