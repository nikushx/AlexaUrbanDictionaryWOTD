import requests

#Request urbandictionary
r = requests.post("http://www.urbandictionary.com/")

#Set s equal to the html
s = r.text

#Split each line into lists
lines = s.split("\n")

#Sort through lines and find first word on homepage
for lineNum in range(len(lines)):
    if lines[lineNum].startswith("<a class=\"word\""):
        result = lines[lineNum]
        break

#Grab word from line by shifting out the data and leaving just the word
start = result.index(">") + 1
end = result.rindex("<")
topWord = result[start:end]

#Get def from 3 lines ahead - refer to testfile
resultDef = lines[lineNum + 3]