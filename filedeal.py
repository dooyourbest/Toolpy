#!/usr/bin/env python
# coding=utf-8
from count import Count
class FileDeal:
	def __init__(self):
		self.filePath=''
		self.outPutPath=''
	def setConf(self,name='',path='',outPutPath=''):
		self.fileName=name
		self.filePath=path
		self.outPutPath=outPutPath
	def load(self,pathname):
		self.filePath=pathname
		self.file=open(self.filePath)
	def save(self,file,content):
		tmpfile=open(self.outPutPath,'a');
		tmpfile.write(content);
		tmpfile.close()
	def getRow(self,rowList=False):
		self.list=self.file.readlines();
		allLineNum = len(self.list)
		tmpArr=[]
		if rowList==False:
			for  i in range(1,allLineNum):
				tmpArr.append(self.list[i-1])
			return tmpArr;
		for line in rowList:
			rowListDict[line]=1
		for  i in range(1,allLineNum):
			if i in rowListDict:
				tmpArr.append(self.list[i-1])
		return tmpArr

	def getCol(self, list, number, limitStr=' '):
		tmpArr=[]
		for line in list:
			line=line.strip()
			arr=line.split(limitStr);
			tmpArr.append(arr[number-1])
		return tmpArr
	def getAllLineNum(self):
		return len(self.file.readlines())


# count=Count()
# file=FileDeal()
# file.load('line_road.txt');
# list=file.getRow()
# res=file.getCol(list,5,',')
# min,max=count.getminmax(res);
# alldict=count.countList(res);
# x,y=count.sortedDictValues(alldict)
# print x
# print y
# exit()


