
import csv

import re

d={}
def csvToDictionary():
    reader = csv.reader(open('french_dictionary.csv', 'r'))
    d = {}
    for row in reader:
       k, v = row
       d[k] = v
    return d
    

def textToList():
    my_file = open("find_words.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    for i in content_list:
        if i not in d.keys():
            content_list.remove(i)
    my_file.close()
    return content_list


def inputToList():
    my_file = open("t8.shakespeare.txt", "r")
    content = my_file.read()
    my_file.close()
    return content    


if __name__ == "__main__":
    csvDict=csvToDictionary()  
    text=textToList()
    inputFile=inputToList()
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in text:    
            entry=[]
            n=inputFile.count(i)
            if(n>0):
                #inputFile=inputFile.replace(i,csvDict[i])
                inputFile=re.sub(re.escape(i), csvDict[i], inputFile, flags=re.IGNORECASE)
                entry.append(i)
                entry.append(csvDict[i])
                entry.append(n)
                writer.writerow(entry)
        print(inputFile)        
    resultFile = open("resultFile.txt", "w")
    resultFile.write(inputFile)

