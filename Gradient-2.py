#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Example 1
# f(x)=x^2 +x +1

# In[2]:


def f(x):
    return x**2 + x+1


# In[3]:


f(1)


# In[4]:


#data generating
x_1=np.linspace(start=-300, stop=300, num=10000)


# In[5]:


x_1


# In[6]:


x_1[0]


# In[7]:


g2=1
for i in range (0,10000):
    g1=abs(f(x_1[i]))
    if g2>=g1:
        g2=g1
        print(f'x_1[{i}]={x_1[i]} and g1 = {g1}')
print(f'the minmum f(x) is {g2}')


# In[8]:


#plot
plt.plot(x_1,f(x_1))


# In[9]:


#plot
plt.xlim([-3,3])
plt.ylim([-.2,2])
plt.xlabel('X',fontsize=17)
plt.ylabel('f(x)',fontsize=17)
plt.plot(x_1,f(x_1))


# ## slope and Derivatives
# 

# In[10]:


def d(x):
    return 2*x+1


# In[11]:


#plot & deritives
plt.figure(figsize=[5,15])
plt.subplot(2,1,1)
plt.xlim([-3,3])
plt.ylim([-3,3])
plt.xlabel('X',fontsize=17)
plt.ylabel('f(x)',fontsize=17)
plt.plot(x_1,f(x_1))
plt.title("cost function")
#derivative:
plt.subplot(2,1,2)
plt.xlim([-3,3])
plt.ylim([-3,3])
plt.xlabel('X',fontsize=17)
plt.ylabel('d(x)',fontsize=17)
plt.plot(x_1,d(x_1))
plt.title("slope of cost function")
plt.grid()


# ## python loops and Gradient Descent 

# In[12]:


new_x=3
previous_x=0
step=0.1
precision=0.000001
for n in range(1000):
    previous_x=new_x
    gradient=d(previous_x)
    new_x=previous_x-step*gradient
    difference=abs(new_x-previous_x)
    if difference<=precision:
        print("loop ran this many times",n)
        break
print(new_x)
print(f(new_x))
print(gradient)


# ## visualisation

# In[13]:


new_x=3
previous_x=0
step=0.1
precision=0.000001
x_list=[]
d_list=[]
for n in range(1000):
    previous_x=new_x
    gradient=d(previous_x)
    new_x=previous_x-step*gradient
    difference=abs(new_x-previous_x)
    x_list.append(new_x)
    d_list.append(gradient)
    if difference<=precision:
        print("loop ran this many times",n)
        break
print(new_x)
print(f(new_x))
print(gradient)


# In[14]:


#plot & deritives
plt.figure(figsize=[5,15])
plt.subplot(2,1,1)
plt.xlim([-3,3])
plt.ylim([-3,3])
plt.xlabel('X',fontsize=17)
plt.ylabel('f(x)',fontsize=17)
plt.plot(x_1,f(x_1))
values=np.array(x_list)
plt.scatter(values, f(values), color='red')


# ## Multiple minimum vs initial guess and advanced function
# ### $$ g(x)=x^4-4x^2+5$$

# In[16]:


x_2= np.linspace(-2,2,1000)


# In[25]:


def g(x):
    return x**4-4*x**2+5
def dg(x):
    return 4*x**3-8*x


# In[46]:


new=2
previous=0.0
prec=0.01
step=0.1
for i in range(1000000):
    previous=new
    d1=dg(previous)
    new=previous-step*d1
    difference= abs(new-previous)
    if difference<=prec:
     break
print("the minimum occurs in=",new)
print("the minmum amount of function is",g(new))


# In[42]:


plt.plot(x_2,g(x_2))


# ## gradient descent as a python function

# In[53]:


def grad(dg_function, start,step=0.2,prec=0.1):

    new=start
    previous=0.0
    for i in range(1000000):
        previous=new
        d1=dg_function(previous)
        new=previous-step*d1
        difference= abs(new-previous)
        if difference<=prec:
         break
        return new


# In[56]:


new=grad(dg,1,0.1,0.001)
print("x",new)
print("g(x)=",g(new))


# In[ ]:




