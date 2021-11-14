"""
@author: Aakash Babu
"""
import cv2
import os


def create_image(name):
    BASE_DIR = os.getcwd()

    image_dir = os.path.join(BASE_DIR, "images")
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_dir = os.path.join(image_dir,name)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # ---------------------- #

    cam = cv2.VideoCapture(0)

    
    # ---------------------- #
    '''
    for root, dirs, files in os.walk(image_dir):
        img_counter = len(files)
    '''
    count = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            # print("failed to grab frame")
            break
        cv2.imshow("DataSet Creator for {} Press Spacebar to click photo and esc key to stop".format(name),frame)


        k = cv2.waitKey(1)
        if k%256 == 27:
            break
        elif k%256 == 32:
            img_name = "{}--{}.png".format(name,count)
            img_dir = os.path.join(image_dir,img_name)
            cv2.imwrite(img_dir, frame)
            count = count+1
            print(15*"#"+img_dir+15*"#")
    cam.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
	print("Import Only File")