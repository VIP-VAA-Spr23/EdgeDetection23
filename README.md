# VIP-EdgeDetection
## Overview
**Purpose**: Determine which and how many bounding boxes that are detected by the localizer are true detections or not.

**Input**:

* Folder of full frame image inputs.
* Json file corresponding to the folder that includes filenames of all the full frame images and the location for each image location for each image

**Output:**
* List showing bounding boxes that are true detections and false detections

Instructions for each file:

File: createLOCS.py
	
	Insert json file folder path where comment shows and enter the path for the full frame images.
	
	This file will parse the latidude locations from the json file and its corresponding filenames.
	It will create a new file called name_Pairs.csv that stores tuples of the file name and its latitude.
	Then, the file will creates new folder called ImgLocs which is in the VIP directory. This folder contains
	a seperate folder for every different location. Inside each location folder, there sets of images that
	under its specific locations.

	The user would now have to manually pick out the empty image frames from each location and add it to a new folder.
	However, since I have already done that created a new folder called GndLocs that contains an empty image frame for each location,
	there is no need.
	
File: bbsDimensions.py

	Enter the path for the folder containing a csv file of bounding boxes for each filename. That folder is stored by variable name bbs_csv.
	Enter the path for the folder that you manually created called GndLocs which is stored into gnd_locs.
	
	This file will create a file called gnd_pairs.csv. This csv file contains filtered pairs that will only contain tuples of filenames
	and its locations only for the manually selected ground truth locations.
	It will also create another csv file called bbsTP.csv that contains tuples of filenames and bounding box dimensions. Since there are multiple bounding boxes per image,
	the file name is repeated for each bounding box it contains. This csv file will be used to extract the dimensions to draw bounding boxes.
	
File: drawGNDBox.py
	
	This file contains two functions that involve creating bounding boxes. The first function createBOX() creates and returns a cropped image representing a boundin box.
	It needs to take two arguments which include the dimension list and the image to be cropped. This function is called in the second function that is created.
	The second function is called getImages(). This function takes the bbsTP list and the specific bounding box to test as arguments. It outputs returns two cropped images.
	One image is the bounding box in the empty frame. The other image is the actual bounding box with the animal.
	
File : checkBBS.py
	
	This file prints out a list of True and false detections. It calls the getImages() function for each bounding box in the bbsTP file.
	Then it calls the getEdges function from edgeDetection file to determine the number of edges in the image. The number of edges for the empty bounding box and the
	detected bounding box. If there is a significant change in the number of edges, then the boundin box is a correct detecion.
	
