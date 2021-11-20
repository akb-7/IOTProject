import warnings
warnings.simplefilter("ignore")
from facerecog.createimage import create_image
from facerecog.trainimage import train_image
from facerecog.runfunction import runmethod

def instruct():
	'''
		General instruction to command line
	'''
	print(20*"-")
	print("\nWelcome to Open CV based face recognition system.\n")
	print(20*"-")

def main():		
	choice = int(input("Enter the choice \n 1.Train the model \t 2. Run the model\n"))
	if choice==1:
		name = input("Enter the name of the human\t")
		print("[INFO] Creating the training image for {}".format(name))
		create_image(name) # this method open up the webcam to capture the train data
		print("[INFO] Started training on the images")
		train_image() # this method train the classifier with the captured image
		print("[INFO] Training completed")
	runmethod()
if __name__=="__main__":
	instruct()
	main()
