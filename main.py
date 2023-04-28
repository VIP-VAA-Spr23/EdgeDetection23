#from edgeCount import getEdges
from edgeDetection import generateImg, getEdges
from drawGNDBox import getImages
import os
import csv


if __name__ == '__main__':

    gnd_locs = os.listdir("C:/Users/krish/OneDrive/Desktop/VIP/GndLocs")
    with open('bbsTP.csv', 'r', newline='') as csvfile:
    # Create a CSV reader object
        reader = csv.reader(csvfile)
        bbsTP = list(reader)
    
    with open('gnd_pairs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        gnd_pairs = list(reader)
    names = [ele[0] for ele in gnd_pairs]
    
    trueDetect = []
    for i in range(len(bbsTP)):
        img1, img2 = getImages(bbsTP, gnd_pairs, names, gnd_locs, i)
        
        bbImg = generateImg(img1)
        count1 = getEdges(bbImg)
        locImg = generateImg(img2)
        count2 = getEdges(locImg)
        diff = abs(count1-count2)
        change = 0
        if count2 > 0:
            change = diff / count2
        if change > 0.30:
            trueDetect.append(True)
        else:
            trueDetect.append(False)
    print(trueDetect)
    
        