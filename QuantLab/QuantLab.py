
# coding: utf-8

# In[40]:

import csv
from collections import defaultdict

#dictionary which stores all unique symbols
dict = defaultdict(list)

with open('input.csv', newline='') as csvfile:
    tradereader = csv.reader(csvfile, delimiter=',', quotechar="|")
    for row in tradereader:
        #check if symbol is unique
        if not row[1] in dict:
            #initialize dict
            dict[row[1]] = [int(row[0]), 0, int(row[2]), int(row[2])*int(row[3]), int(row[3])]
        else:
            #update volume
            dict[row[1]][2] += int(row[2])
            #update avg price
            dict[row[1]][3] += int(row[2])*int(row[3])
            #update max price
            if dict[row[1]][4] < int(row[3]):
                dict[row[1]][4] = int(row[3])
            
            #update max difference timestamp
            if int(row[0]) - dict[row[1]][0] > dict[row[1]][1]:
                dict[row[1]][1] = int(row[0]) - dict[row[1]][0]
                dict[row[1]][0] = int(row[0])


with open('output.csv', 'w', newline='') as csvfile:
    tradewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for key, value in sorted(dict.items()):
        tradewriter.writerow( (key, value[1], value[2], int(value[3]/value[2]), value[4]))

