#!/usr/bin/env python3
import re
import sys
import subprocess
import os

#directoryToGet = sys.argv[1]

def createFileList(dirPath):
	fileList = os.listdir(dirPath)
	shortFileList = []
	for entry in fileList:
		shortEntry = entry[0:10:]
		shortFileList.append(shortEntry)
	return shortFileList

#inputFile = 'SraRunTable.txt'

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
#		if itemDesc in fileDict.keys():	
#			fileDict[itemDesc].append(itemID)
#		else:
#			fileDict[itemDesc] = [itemID]
	return fileDict



def sampleIDTable(fileDict):
	for item in fileDict:
		print('{}\t{}'.format(item, fileDict[item]))	

#	if fileDict[item] not in fileDict.values():
#			print('{}\t{}\t{}'.format(item, fileDict[item], 1))
#		if fileDict[item] in fileDict.values():
#			count = 0
#			count += 2
#			print('{}\t{}\t{}'.format(item, fileDict[item], count))
#
#		if fileDict[item] in fileDict.values()
#	for item in fileDict:
	
#		if for entry in fileList:
#			if entry is in line:
#				print(line)
#			else: 

fastqFileList = createFileList('../data/test/')
#print(fastqFileList)

#inputFile = sys.argv[1]
inputFile = open('./SraRunTable.txt', 'r')

extractFileDict = createFileDict(fastqFileList, inputFile)
#print(extractFileDict)
#print(extractFileDict['wt'])
#print(extractFileDict['wt'][1])
final = sampleIDTable(extractFileDict)

