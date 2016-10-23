import csv
import os
import math
import matplotlib.pyplot as plt
from collections import Counter
import numpy
import glob

dir = os.path.dirname(__file__)

class Main:
    def main(self):
        self.dataSetInformationParse()
        path = "datasets/080725"
        filename = os.path.join(path, '0.txt')
        with open(filename, 'r') as f:
            for line in f:
                print line


    def dataSetInformationParse(self):
        print "Parsing and Graphing Dataset Information..."
        rows = []
        filename = os.path.join(dir, 'Dataset_Information.csv')
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if (reader.line_num != 1):
                    rows.append(row)
        totalNumVideos = 0
        valsX = []
        valsY = []
        for row in rows:
            totalNumVideos+=int(row[3])
            valsX.append(row[0])
            valsY.append(row[3])
        print "Total Number of Videos Crawled: ", totalNumVideos
        plt.scatter(valsX, valsY, label='Crawl', color='k')
        plt.plot(valsX, valsY)
        plt.xlabel('Crawl ID')
        plt.ylabel('Number of Videos')
        plt.title('Number of Videos Crawled')
        plt.legend()
        plt.show()

        #for row in rows:
            #self.parseEachFolder(int(row[0]), row[1])

    def parseEachFolder(self, ID, folderName):
        print "Parsing and Graphing for crawl ID", ID
        rows = []
        path = "datasets/"+ folderName
        #for filename in glob.iglob(os.path.join(path, '*.txt')):
            #with open(filename) as f:
                #for line in f:
        filename = os.path.join(path, 'Dataset_Information.csv')




Main().main()