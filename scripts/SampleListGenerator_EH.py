#!/usr/bin/env python3
import re
import sys
import os

# createFileList function grabs the names of the counts files
# from the counts dir and creates a list using only the
# 10 char SRR ID; required input is path to counts dir
def createFileList(dirPath):
	fileList = os.listdir(dirPath)
	shortFileList = []
	for entry in fileList:
		shortEntry = entry[0:10:]
		shortFileList.append(shortEntry)
	return shortFileList


# createFileDict function creates file dictionary matching 
# experimental description ('strain' from file SraRunTable)
# and matches it to the SRR ID from file list; requires
# file list and path to input file (SraRunTable.txt)
def createFileDict(fileList, inputFile):
	extractFileList = []
	for line in inputFile:
		found = re.search(r'.+(SRR\d+).+', line)
		if not found:
			pass
		else:
			if found.group(1) in fileList:
				extractFileList.append(found.group(0))
	fileDict = {}
	for item in extractFileList:
		itemList = item.split('\t')
		itemID = itemList[11]
		itemDesc = itemList[15]
		fileDict[itemID] = itemDesc
#hashed out lines below could have been used to make dict of lists with desc as key
#		if itemDesc in fileDict.keys():	
#			fileDict[itemDesc].append(itemID)
#		else:
#			fileDict[itemDesc] = [itemID]
	return fileDict


#sampleIDTable function prints two column table with 
#SRR ID and experimental description on same lane, replicate info
#will need to be added in R (by Kirsten?); required input dict
#of matched SSR ID(key) and experimental description(value)
def sampleIDTable(fileDict):
	for item in fileDict:
		print('{}\t{}'.format(item, fileDict[item]))	
