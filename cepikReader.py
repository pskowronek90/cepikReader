from matplotlib import pyplot as plt
from datetime import datetime
from json import load
import json
import os
import shutil
from numpy import invert
import pandas as pd

reportsPath = "./reports"
timeStamp = str(datetime.now().strftime("%Y%m%d%H%M%S"))

class CepikReader():
    #Constructor
    def __init__(self, json):
        self.json = json


    #Read JSON content and presents as graph
    def readJson(self):
        jsonFile = open(self.json)
        jsonData = load(jsonFile)

        #Convert JSON array to key value pairs
        flattenData = {}
        
        for i in jsonData:
            if i['brand'] is None:
                continue
            
            flattenData[i['brand']] = i['amount']

        json.dumps(flattenData)

        #Graph configuration
        brands = list(flattenData.keys())
        amounts = list(flattenData.values())
        
        fig, ax = plt.subplots(figsize=(16, 12)) #Width, height
        ax.invert_yaxis()

        for i, v in enumerate(amounts):
            ax.text(v + 0.1, i + .50, str(v), color='black') 
        
        plt.title('Most popular cars registered')
        plt.barh(brands, amounts, color='green')
        plt.show()

    #Converts filtered JSON data to Excel
    def topBrandsReport(self):
        print("Preparing Top Brands Excel file...")
        
        jsonFile = open(self.json)
        jsonData = load(jsonFile)

        filteredData = [x for x in jsonData if x['amount'] >= 5]
        
        with open('top.json', 'w') as outfile:
            json.dump(filteredData, outfile)
        
        jsonFile = pd.read_json('top.json')
        jsonFile.to_excel('top-' + timeStamp + '.xlsx')

        self.removeTempFile()
        self.moveReports()


    #Converts entire JSON data to Excel
    def fullReport(self):
        print("Preparing Full Excel file...")
        
        jsonFile = pd.read_json(self.json)
        jsonFile.to_excel('full-' + timeStamp + '.xlsx')

        self.moveReports()

    #Move reports to dedicated folder
    def moveReports(self):
        reportExtensions = (".xls", ".xlsx")
        
        if not os.path.exists(reportsPath):
            os.mkdir(reportsPath)
        
        for file in os.listdir("."):
            if file.endswith(tuple(reportExtensions)):
                shutil.move(file, os.path.join(reportsPath))

    def removeTempFile(self):
        os.remove('top.json')

# #Testing
JSONReader = CepikReader('test.json')
JSONReader.readJson()
