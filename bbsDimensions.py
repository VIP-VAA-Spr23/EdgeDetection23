import os
import csv


if __name__ == "__main__":
    outputPath = os.path.abspath('outputs_csv/outputs_csv')
    bbs_csv = os.listdir(outputPath) #takes in directory of csv files for each image with each containing bounding box dimensions
    gnd_locs = os.listdir("GndLocs")#Enter file path for manually created folder of all the location images
    
    with open('name_Pairs.csv', 'r', newline='') as csvfile: #reads and retreives a list of filename to location tuples
    # Create a CSV reader object
        reader = csv.reader(csvfile)
        pairs = list(reader)

    #this segment filters out the name_Pairs.csv by only including pairs with locations that are in the gnd_locs folder and saving it to gnd_pairs list
    gnd_pairs = []
    for loc in gnd_locs:
        loc = loc.split(".jpg")[0]
        for pair in pairs:
            if loc in pair[1]:
                gnd_pairs.append(pair)

    with open('gnd_pairs.csv', 'w', newline='') as csvfile: #writes the gnd_pairs list into gnd_pairs.csv
        writer = csv.writer(csvfile)
        writer.writerows(gnd_pairs)

    csv_bbs = []
    for pair in gnd_pairs: #loops through each pair in gnd_pairs
        name = pair[0]
        name = name.replace(".jpg", ".csv")
        idx = bbs_csv.index(name)
        csv_bbs.append(bbs_csv[idx]) #appends csv file of bounding box dimensions for every image in gnd_pairs

    bbsFiles = []
    nameCSV = []
    for i in range(len(csv_bbs)):
        csv_path = os.path.join(outputPath, csv_bbs[i])
        with open(csv_path, mode="r") as csv_file: #opens and reads csv file from gnd_pairs
            reader = csv.reader(csv_file, delimiter=',') #seperates the commas in the dimension list
            csvRows = []
            names = []
            for row in reader: #loops through every bounding box dimension in list of dimensions
                csvRows.append(row) #appends dimensions
                names.append(csv_bbs[i]) #file name for which the bounding box is part of
            csvRows.pop(0)
            names.pop(0)
        bbsFiles.append(csvRows) #appends all the dimension rows to bbsFiles for each image file
        nameCSV.append(names) #appends list of image files

    bbsFiles = [ele for ele in bbsFiles if ele != []] #removes elements that are empty lists
    
    bbsFiles = sum(bbsFiles, []) #concatenates all the lists in bbsFiles into one list
    nameCSV = sum(nameCSV, []) #concatenates all lists together
    bbsTP = tuple(zip(nameCSV, bbsFiles)) #creates tuples of filenames to its bounding box dimensions

    with open('bbsTP.csv', 'w', newline='') as csvfile: #saves bbsTP to bbsTP.csv
        writer = csv.writer(csvfile)
        writer.writerows(bbsTP)
    