import json
import os
import cv2
import csv

def main():
    with open("C:/Users/krish/Downloads/labeled_file_info.json", 'r') as f:
        data = json.load(f)
    names = [d["filename"] for d in data]
    locations = [d["latlon"] for d in data]
    latr = [loc[0] for loc in locations]
    longs = [longs[1] for longs in locations]
    longs = list(set(longs))
    lats = list(set(latr))
    coords = list(zip(lats, longs))
    print(len(data))
    name_Pairs = tuple(zip(names, latr))
    with open('name_Pairs.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
        writer = csv.writer(csvfile)

    # Write the list of tuples to the file
        writer.writerows(name_Pairs)
    print(len(name_Pairs))
    fileLists = []
    for lat in lats:
        fileNames = []
        for element in data:
            if lat in element["latlon"]:
                fileNames.append(element["filename"])
        fileLists.append(fileNames)
    
    
    imgDir = "C:/Users/krish/Downloads/full_frame_image_inputs/full_frame_image_inputs"
    fullDir = os.listdir(imgDir)
 
    
    i = 0
    for file in fileLists:
        latd = str(lats[i])
        pathDir = os.path.join("C:/Users/krish/OneDrive/Desktop/VIP/ImgLocs", latd)
        os.mkdir(pathDir)
        i+= 1
        for imgName in file:
            idx = fullDir.index(imgName)
            newImg = fullDir[idx]
            imgP = os.path.join(imgDir, newImg)
            img = cv2.imread(imgP)
            cv2.imwrite(os.path.join(pathDir, newImg), img)

    

if __name__ == "__main__":
   main()


