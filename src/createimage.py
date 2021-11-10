# -*- coding: utf-8 -*-

"""
Created on Thu Jun  4 13:30:27 2020

@author: Aakash Babu
"""
from datetime import datetime
import cv2
import os
import warnings
warnings.simplefilter("ignore")

def create_image(name):
    #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    if name is None:
        return
    BASE_DIR = os.getcwd()

    image_dir = os.path.join(BASE_DIR, "images")
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_dir = os.path.join(image_dir,name)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # ---------------------- #

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("DataSet Creator for {}".format(name))

    # ---------------------- #
    '''
    for root, dirs, files in os.walk(image_dir):
        img_counter = len(files)
    '''

    while True:
        ret, frame = cam.read()
        if not ret:
            # print("failed to grab frame")
            break
        cv2.imshow("DataSet Creator for {}".format(name), frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            break
        elif k%256 == 32:
            img_name = "{}--{}.png".format(name,str(datetime.now()))
            img_dir = os.path.join(image_dir,img_name)
            cv2.imwrite(img_dir, frame)
            print(15*"#"+img_dir+15*"#")
    cam.release()
    cv2.destroyAllWindows()
