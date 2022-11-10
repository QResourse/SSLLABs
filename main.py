import ssllabsscanner as ssl
import csv
import os
import json

#Load scan from cache
NewScan = False
DataArray = []
endPointsArray = []
domains = []

RESULT_FILE= os.path.join("export","result.json")
with open('domains.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines[0])
        domains.append(lines[0])
 # displaying the contents of the CSV file



for domain in domains:
    print("starting domain :", domain)
    if (NewScan):    
        data = ssl.newScan(domain)
    else:
        data = ssl.resultsFromCache(domain)
    try:
        endPointsArray = data['endpoints']
    except:
        endPointsArray = []
    
    for endpoint in endPointsArray:
        dataDict = {
                "host" : data['host'],
                "port" : data['port'],
                "protocol" : data['protocol'],
                "isPublic" : data['isPublic'],
                "Status" : data['status'],
                "startTime" : data['startTime'],
                "testTime" : data['testTime'],
                "engineVersion" : data['engineVersion'],
                "criteriaVersion" : data['criteriaVersion'],
                "endpoints" : data['endpoints']
            }
        DataArray.append(dataDict)

print(DataArray)
json_object = json.dumps(DataArray, indent=4)
with open(RESULT_FILE, "w") as outfile:
    outfile.write(json_object)