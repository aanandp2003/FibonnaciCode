#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=int(input("Enter the number of terms you want"))
a=0
b=1
print(a)
print(b)

for i in range(1, x-1):
    c=a+b
    a=b
    b=c
    print(c)
    
    


# In[ ]:




