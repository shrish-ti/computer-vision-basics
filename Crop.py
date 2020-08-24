#!/usr/bin/env python
# coding: utf-8

# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import cv2
im=cv2.imread('colors.jpg')
h,w,c = im.shape
c=im[0:2000,0:2000]
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.imshow(im)
ax1.set_title('Original version')
ax2.imshow(c)
ax2.set_title('Cropped version')


# In[ ]:





# In[ ]:




