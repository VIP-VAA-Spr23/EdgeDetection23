# VIP-EdgeDetection
## Overview
**Purpose**: 

This project focuses on the accuracy of the localizer in identifying the animal detections from the camera footage. The research program has provided a dataset of images and the bounding boxes for each image. A bounding box is a cropped part of the full frame image. The existance of the bounding boxes show the existance of animals present within the bounding box. The goal of this project is to determine if a bounding box is correctly identified by the localizer by seeing if it actually entails an animal in it. An image processing feature detects edges in an image which is used to identify a detection. We are working with a sample set of 203 images containing bounding boxes for each image.

**How it works**:

A set of bounding boxes are processed which is traced back to its corresponding full frame images. Each image has a location of where the image was taken. For ever location in the data, there is an empty image frame that does not have any animals in it. The dimensions of each bounding box is used to crop that exact spot in its corresponding empty image. An empty bounding box is then compared to the true bounding box using the edge detection feature by forming edges around concrete objects but not within the objects in an image. This feature is applied to both the empty bounding box and the true bounding box. The frames with animals will have less edges than the frames without. Therefore, if the empty bounding box detects more edges than the true bounding box, we can reason that the bounding box is a true positive detection.

**Input**: 

* Folder of the 203 full frame image inputs.
* Json file corresponding to the folder that includes filenames of all the full frame images and the location for each image location for each image
* Folder containing csv files for each image that contains bounding box dimensions

**Output:**
* List showing bounding boxes that are true positive detections and false positive detections
### Libraries required:
* json libary- read and parse json files
* os library- read folder directories and create folder paths and new folders 
* cv2 library- work with image processing to perform gaussian blur and dilation
* csv library- process csv files and to extract data as well as create new csv files
* numpy library- create numpy arrays and perform mathematical calculations

## General instructions to test sample set:
I have already provided the data to test the sample bounding boxes and determine correct classifications. The user would only need to run main.py. This requires the user to import the libraries and clone the repository. Make sure gnd_pairs.csv and bbsTP.csv and GndLocs folder is in the explorer of your IDE and run the file. If the user intends on running a different sample set images, then follow the instructions for each file below.
## Instructions for each python file:

### File: createLOCS.py
#### Instructions for testing your own set of bounding boxes: 
* Replace 'labeled_file_info.json' with the file path of the json file you are using for your data set. This file must include coordinates and filename attributes. 
* Replace "full_frame_image_inputs" with the path of your full frame inputs. Make sure both these files are in the same working directory of the scripts. 
* Lastly, create a path for ImgLocs which will be a new folder containing an empty image for location. The folder path has to be similar to the path as the other files in order to be in the same directory. Replace "C:/Users/krish/OneDrive/Desktop/VIP/ImgLocs" with your path.
#### Description	
This script will parse the latidude locations from the json file and its corresponding filenames.
	It will create a new file called name_Pairs.csv that stores tuples of the file name and its latitude.
	Then, the script will create a new folder called ImgLocs which is in the directory. This folder contains
	a set of subfolders for each different location in the data. Inside each location folder, there is a set of images that corresponds to that location.

The user would now have to manually pick out the empty image frames from each location that don't have animals present and add it to a new folder. This folder should be named GndLocs and be placed in the same directory as all the scripts.
	However, since I have already done that created a new folder called GndLocs that contains an empty image frame for each location,
	there is no need.
	
### File: bbsDimensions.py
	
This file will create a file called gnd_pairs.csv. This csv file contains filtered pairs that will only contain tuples of filenames
	and its locations only for the manually selected ground truth locations.
	It will also create another csv file called bbsTP.csv that contains tuples of filenames and bounding box dimensions. Since there are multiple bounding boxes per image,
	the file name is repeated for each bounding box it contains. This csv file will be used to extract the dimensions to draw bounding boxes.
	
### File: drawGNDBox.py
	
This file contains two functions that involve creating the bounding boxes. The first function createBOX() creates and returns a cropped image representing a bounding box.
	It needs to take two arguments which include the dimension list and the image to be cropped. This function is called in the second function that is created.
	The second function is called getImages(). This function takes the bbsTP list and the specific bounding box to test as arguments. Its output returns two cropped images. One image is the bounding box in the empty frame. The other image is the actual bounding box with the animal.
### File: EdgeDetection.py
There are two functions in this file. The funciton generateImg() takes in the bounding box image and transforms it to have edges. The image is than returned and goes into the getEdges() function which returns the number of edges in the image.
	
### File : main.py
	
This file prints out a list of True and false detections. It calls the getImages() function for each bounding box in the bbsTP file.
	Then it calls the getEdges function from edgeDetection file to determine the number of edges in the image. The number of edges for the empty bounding box and the
	detected bounding box. If there is a significant change in the number of edges, then the bounding box is a correct detecion.
	
