# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:22:14 2019

@author: mach0
"""

'''daoruku'''
import cv2
'''jiazairenlianmoxing'''
face=cv2.CascadeClassifier('C:\Users\mach0\Desktop\haarcascade_frontalface_alt.xml')
'''dakaishexiangtou'''
capture=cv2.VideoCapture(0)
'''chuangjianchuangkou'''
cv2.namedWindow('Cam')

'''huoqushexiangtou huamian'''
while True:
    '''duqushexiangtou de zhenhuamian'''
    ret,frame=capture.read()
    '''tiaozhenghuidu to accelerate xuanran'''
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cv2.imshow('HeMa',frame)
    '''jiancharenlian'''
    faces=face.detectMultiScale(gray)
    '''biaoji renlian'''
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('Cam',frame)
    '''zantingchuangkou'''
        if cv2.waitKey(5)&0xFF==ord('q'):
            break
'''shifangziyuan'''
capture.release()
'''guanbishexiangtou'''
cv2.destoryAllWindows()