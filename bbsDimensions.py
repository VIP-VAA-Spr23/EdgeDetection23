import os
import csv
import pickle

if __name__ == "__main__":
    bbs_csv = os.listdir("C:/Users/krish/OneDrive/Desktop/VIP/outputs_csv/outputs_csv") #Enter file path for folder that contains csv files
    gnd_locs = os.listdir("C:/Users/krish/OneDrive/Desktop/VIP/GndLocs")#Enter file path for manually created folder of all the location images
    #img_locs = os.listdir("C:/Users/krish/OneDrive/Desktop/VIP/ImgLocs") 
    
    with open('name_Pairs.csv', 'r', newline='') as csvfile:
    # Create a CSV reader object
        reader = csv.reader(csvfile)
        pairs = list(reader)
        
    gnd_pairs = []
    for loc in gnd_locs:
        loc = loc.split(".jpg")[0]
        for pair in pairs:
            if loc in pair[1]:
                gnd_pairs.append(pair)
    with open('gnd_pairs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(gnd_pairs)

    csv_bbs = []
    for pair in gnd_pairs:
        name = pair[0]
        name = name.replace(".jpg", ".csv")
        idx = bbs_csv.index(name)
        csv_bbs.append(bbs_csv[idx])

    bbsFiles = []
    nameCSV = []
    for i in range(len(csv_bbs)):
        csv_path = os.path.join("C:/Users/krish/OneDrive/Desktop/VIP/outputs_csv/outputs_csv", csv_bbs[i])
        with open(csv_path, mode="r") as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            csvRows = []
            names = []
            for row in reader:
                csvRows.append(row)
                names.append(csv_bbs[i])
            csvRows.pop(0)
            names.pop(0)
        bbsFiles.append(csvRows)
        nameCSV.append(names)

    bbsFiles = [ele for ele in bbsFiles if ele != []]
    #nameCSV = [nameCSV[i] for i in range(len(bbsFiles)) if bbsFiles[i] != []]
    print(len(bbsFiles))
    print(len(nameCSV))
    bbsFiles = sum(bbsFiles, [])
    nameCSV = sum(nameCSV, [])
    print(len(bbsFiles))
    print(len(nameCSV))
    print(type(bbsFiles[1]))
    #bbsDict = {nameCSV[i]: bbsFiles[i] for i in range(len(nameCSV))}
    #print(bbsDict)
    bbsTP = tuple(zip(nameCSV, bbsFiles))

    with open('bbsTP.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(bbsTP)
    #os.mkdir("C:/Users/krish/OneDrive/Desktop/VIP/bbsDict.pk1")
    #with open("C:/Users/krish/OneDrive/Desktop/VIP/bbsDict.pk1", 'wb') as file:
        #pickle.dump(bbsDict, file)