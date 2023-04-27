import os
import csv
import cv2
import numpy as np

def main():
    img_Fold = "C:/Users/krish/Downloads/newImgs/Krishna"
    files = os.listdir(img_Fold)

    for img in files:
        pathImg = os.path.join(img_Fold, img)#create path with downloads folder and image extension
        generateImg(pathImg)

def getEdges(img):



    edges = cv2.Canny(img, 100, 200)


    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    edges = len(contours)
    return edges    
 
def generateImg(pathImg):
    #cvImg = cv2.imread(pathImg)
    #grayImg = cv2.cvtColor(pathImg, cv2.COLOR_BGR2GRAY)#convert to grayscale
    imgG = cv2.GaussianBlur(pathImg,(5,5),0)#Gaussian blur on image
    #lapImg = cv2.Laplacian(img,cv2.CV_64F)
    #sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(imgG,cv2.CV_64F,0,1,ksize=5)#type of edge detection
    
    #black_pix = np.sum(sobely == 0)
    #cv2.imwrite(os.path.join("C:/Users/krish/Downloads/edgeDetectImgs", img), sobely)

    edges = cv2.Canny(imgG, 50, 150)

    # Dilate the edges to make them thicker
    kernel = np.ones((3,3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # Invert the dilated image
    inverted = cv2.bitwise_not(dilated)

    # Convert the inverted image to a color image
    color = cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)

    # Draw lines on the color image
    '''
    lines = cv2.HoughLinesP(inverted, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(color, (x1, y1), (x2, y2), (0, 0, 255), 1)
'''
    # Save the output image
    #cv2.imwrite(os.path.join("C:/Users/krish/Downloads/edgeDetectImgs", img), color)
    return color

if __name__ == '__main__':
    main()