#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
import random


# In[2]:


creeper = np.full((720,720,3), 255, dtype="uint8")


# In[3]:


greens = [[204, 255, 204], #lighter to darker shades of green
          [153, 255, 153],
          [102, 255, 102],
          [51, 255, 51], 
          [0, 255, 0], 
          [0, 204, 0], 
          [0, 153, 0], 
          [0, 102, 0]]


# In[4]:


for i in range(0,720,90):
    for j in range(0,720,90):
        color = random.choices(greens, k=1)[0]
        creeper[i:i+90, j:j+90] = color 
        
creeper[90:270, 90:270] = [0, 0, 0]
creeper[90:270, 450:630] = [0, 0, 0]
creeper[270:360, 270:450] = [0, 0, 0]
creeper[360:540, 180:540] = [0, 0, 0]
creeper[540:630, 180:270] = [0, 0, 0]
creeper[540:630, 450:540] = [0, 0, 0]


# In[5]:


plt.imshow(creeper)


# In[6]:


cv2.imshow("creeper.jpg", creeper)
cv2.waitKey()
cv2.destroyAllWindows()


# In[7]:


enderman = np.full((720,720,3), 0, dtype="uint8")


# In[8]:


purples = [[236, 116, 255], [204, 0, 204], [237, 140, 255]]


# In[9]:


enderman[360:450, 0:90] = enderman[360:450,630:720] = purples[0]
enderman[360:450, 90:180] = enderman[360:450,540:630] = purples[1]
enderman[360:450, 180:270] = enderman[360:450,450:540] = purples[2]


# In[10]:


plt.imshow(enderman)


# In[11]:


cv2.imshow("enderman.jpg", enderman)
cv2.waitKey()
cv2.destroyAllWindows()


# In[46]:


img1 = creeper.copy()
img2 = enderman.copy()
temp = img2.copy()[:,360:720]
img2[:,360:720] = img1.copy()[:,360:720]
img1[:,360:720] = temp.copy()[:]


# In[47]:


plt.imshow(img1)


# In[48]:


plt.imshow(img2)


# In[53]:


collage = np.hstack((creeper, enderman))


# In[54]:


plt.imshow(collage)

