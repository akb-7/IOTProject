# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 23:43:54 2020

@author: Aakash Babu
"""


import warnings
warnings.simplefilter("ignore")  
import cv2
import pickle

def runmethod():
    face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("./recognizer/face-trainner.yml")
    labels = {"person_name": 1}
    with open("pickle//face-labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors=5,minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        
        for(x,y,w,h) in faces:
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            
            id_, conf = recognizer.predict(roi_gray)  
            if conf>=35 and conf <= 75:
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_] + str(conf)
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            
            color = (255,0,0)
            stroke =2
            end_cord_x = x+w
            end_cord_y = y+h
            cv2.rectangle(frame , (x,y) , (end_cord_x,end_cord_y),color,stroke)
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()