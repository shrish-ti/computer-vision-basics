#!/usr/bin/env python
# coding: utf-8

# In[28]:


import cv2
import matplotlib.pyplot as plt 
im=cv2.imread('colors.jpg')
w=im.shape[1]
b=[]
r=[]
g=[]
for i in range(w):
 b.append(im[0,i,0])
 r.append(im[0,i,1])
 g.append(im[0,i,2])
pix=[i for i in range(0,w)]
plt.plot(pix,b)
plt.plot(pix,r)
plt.plot(pix,g)
plt.show()
    


# In[ ]:





# In[ ]:




