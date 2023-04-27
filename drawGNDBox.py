import os
import csv
import cv2

def createBOX(dim, img):
    x = dim[0]
    y = dim[1]
    w = dim[2]
    h = dim[3]
    width, height = img.shape[1], img.shape[0]

    x = int(x*width)
    y = int(y*height)
    w = int(w*width)
    h = int(h*height)

    #image = cv2.rectangle(img, (x, y), (x+w, y+h), color=(0,255,0), thickness=2)
    cropped_image = img[y:y+h, x:x+w]
    return cropped_image 


if __name__ == "__main__":
    gnd_locs = os.listdir("C:/Users/krish/OneDrive/Desktop/VIP/GndLocs")
    with open('bbsTP.csv', 'r', newline='') as csvfile:
    # Create a CSV reader object
        reader = csv.reader(csvfile)
        bbsTP = list(reader)
    v = 91
    with open('gnd_pairs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        gnd_pairs = list(reader)
    names = [ele[0] for ele in gnd_pairs]

def getImages(bbsTP, gnd_pairs, names, gnd_locs, v):
    dim = bbsTP[v][1]
    dim = [float(i.strip("'")) for i in dim.strip("[]").split(", ")]
    
    n = bbsTP[v][0].replace('.csv', '.jpg')
    bbPath = os.path.join("C:/Users/krish/Downloads/full_frame_image_inputs/full_frame_image_inputs", n)
    bbImg = cv2.imread(bbPath, 0)
    #cv2.imshow('bruh', bbImg)
    image = createBOX(dim, bbImg)
    #cv2.imshow('uo', image)
    
    if n in names:
        idx = names.index(n) 
        loc = gnd_pairs[idx][1] + '.jpg'
        
        if loc in gnd_locs:
            path = os.path.join("C:/Users/krish/OneDrive/Desktop/VIP/GndLocs", loc)
            img = cv2.imread(path, 0)
            #cv2.imshow('ds', img)
            img = createBOX(dim, img)
            #cv2.imshow('loc', img)
            #cv2.waitKey(0)
    return image, img
    