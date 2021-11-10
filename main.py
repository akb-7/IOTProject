import warnings
warnings.simplefilter("ignore")
from src.createimage import create_image
from src.trainimage import train_image
from src.runfunction import runmethod

def main():
	''' Driver function that connects all the dots😎😎😎'''
	name = input("Enter the name of the candidate  ")
	print("[INFO] Creating the training image for {}".format(name))
	create_image(name) # this method open up the webcam to capture the train data
	print("[INFO] Escape key pressed Started training on the images")
	train_image() # this method train the classifier with the captured image
	print("[INFO] Training completed")
	runmethod()
main()
