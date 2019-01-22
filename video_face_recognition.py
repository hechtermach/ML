# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#'''daoruku'''
import cv2
#'''jiazairenlianmoxing'''
face=cv2.CascadeClassifier(r'C:\Users\mach0\Desktop\haarcascade_frontalface_alt.xml')
#'''buzhuoshexiangtou'''
capture=cv2.VideoCapture(0)
#'''chuangjianchuangkou'''
cv2.namedWindow('Cam')
#'''huoqushexianghuamian'''
while True:
#    '''duqu shexiangtou zhenhuamian'''
    ret,frame=capture.read()
#    '''tiaozhenghuamianweihuidu jiasuxuanran'''
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
#    '''jiancharenlian'''
    faces=face.detectMultiScale(gray,1.1,3,0,(100,100))
#    '''biaojirenlian'''
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('Cam',frame)
#        '''zantingchuangkou'''
        if cv2.waitKey(5)&0xFF==ord('q'):
            break
#'''shifangziyuan'''
capture.release()
#'''guanbichuangkou'''
cv2.destoryAllWindows()