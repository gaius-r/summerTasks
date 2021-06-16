#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import numpy
import cv2
import pickle


# In[ ]:


port = 2222
ip = '127.0.0.1'


# In[ ]:


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((ip, port))
    while True:
        conn = s.recvfrom(100000000)
        data, client_ip = conn
        print(data)
        if data == b'terminated' or cv2.waitKey(10) == 13:
            break
        data = pickle.loads(data)
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
        cv2.imshow('VideoCAP', frame)
        
    cv2.destroyAllWindows()


# In[ ]:




