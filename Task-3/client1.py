#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import numpy
import cv2
import pickle


# In[ ]:


s_port = 2222
s_ip = "127.0.0.1"


# In[ ]:


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10000000)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('client', frame)
        ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY),30])
        buffer_as_bytes = pickle.dumps(buffer)
        s.sendto(buffer_as_bytes, (s_ip, s_port))
        if cv2.waitKey(10) == 13:
            s.sendto(b'terminated',(s_ip, s_port))
            break
    cv2.destroyAllWindows()
    cap.release()


# In[ ]:




