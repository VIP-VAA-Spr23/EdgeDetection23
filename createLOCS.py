import json
import os
import cv2
import csv

def main():
    with open('labeled_file_info.json', 'r') as f: #replace 'labeled_file_info.json' with the file path for your json file
        data = json.load(f)
    names = [d["filename"] for d in data] #extract filename for each element in file
    locations = [d["latlon"] for d in data] #extract coordinates for each element
    latr = [loc[0] for loc in locations] #extract latitude for each coordinate
    longs = [longs[1] for longs in locations]
    longs = list(set(longs))
    lats = list(set(latr)) #list of all the unique location latitudes in the data
    
    
    name_Pairs = tuple(zip(names, latr)) #pair file names to its corresponding latitude 
    with open('name_Pairs.csv', 'w', newline='') as csvfile: #write to new csv file
    # Create a CSV writer object
        writer = csv.writer(csvfile)
    # Write the list of tuples to the file
        writer.writerows(name_Pairs)

    #This segment creates a list of unique locations that contains a seperate list of file names for each unique location
    fileLists = []
    for lat in lats: 
        fileNames = []
        for element in data:
            if lat in element["latlon"]:
                fileNames.append(element["filename"])
        fileLists.append(fileNames)
    
    
    imgDir = "full_frame_image_inputs" #folder of full frame images
    fullDir = os.listdir(imgDir)
    
    
    i = 0
    for file in fileLists: #loops through every location list
        latd = str(lats[i])
        pathDir = os.path.join("C:/Users/krish/OneDrive/Desktop/VIP/ImgLocs", latd) #create a folder for path for ImgLocs that contains a seperate folder for each location
        
        os.mkdir(pathDir) #creating the directory
        i+= 1
        for imgName in file: #loops through every img name in location list
            idx = fullDir.index(imgName)
            newImg = fullDir[idx]
            imgP = os.path.join(imgDir, newImg)
            img = cv2.imread(imgP)
            cv2.imwrite(os.path.join(pathDir, newImg), img) #creates a folder of locations that has a seperate folder for each location with its corresponding image files.

    

if __name__ == "__main__":
   main()


