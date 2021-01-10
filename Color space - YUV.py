#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import matplotlib.pyplot as plt
im=cv2.imread('very-trippy.jpg')
plt.imshow(im)
img_yuv = cv2.cvtColor(im, cv2.COLOR_BGR2YUV)
plt.imshow(img_yuv)


# In[ ]:




