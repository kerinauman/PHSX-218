#!/usr/bin/env python
# coding: utf-8

# In[9]:


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
V = np.array([3.58, 5.93,7.63,8.78,9.57,10.09,10.45,10.70,10.87,10.98,11.06,11.12]) 
t = np.array([10,20,30,40,50,60,70,80,90,100,110,120])
plt.plot(t, V)

plt.xlabel('Voltage (V)')
plt.ylabel('Time (sec)')
plt.title('Charging Circuit')


# In[10]:


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
V = np.array([8.20,5.71,3.92,2.66,1.82,1.29,0.90,0.63,0.45,0.31,0.23,0.16]) 
t = np.array([10,20,30,40,50,60,70,80,90,100,110,120])
plt.plot(t, V)

plt.xlabel('Voltage (V)')
plt.ylabel('Time (sec)')
plt.title('Discharging Circuit')


# In[ ]:




