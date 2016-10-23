import csv
import os
import math
import matplotlib.pyplot as plt
from collections import Counter
import numpy

dir = os.path.dirname(__file__)

class Main:
    def main(self):
        self.dataSetInformationParse()

    def dataSetInformationParse(self):
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
        plt.xlabel('Crawl ID')
        plt.ylabel('Number of Videos')
        plt.title('Number of Videos Crawled')
        plt.legend()
        plt.show()




Main().main()