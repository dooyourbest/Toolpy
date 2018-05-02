#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt  
class Plot:
    def __init__(self):
        self.xList=[]
        self.yList=[]
        self.xnote=[]
        self.ynote=[]
        self.note=[]
        self.right=[]
    def setXY(self,x,y):
        self.xList=x
        self.yList=y
    def setTitle(self,msg):
        self.title=msg
    def setdot(self,x,y,str):
        self.xnote=x
        self.ynote=y
        self.note=str
    def printZhexian(self,save=True,name='test'):
        plt.plot(self.xList,self.yList)
        for line in range(len(self.xnote)):
            plt.text(self.xnote[line],self.ynote[line],self.note[line])
        plt.title(self.title);
        # plt.show()
        if save:
           plt.savefig(name)
           plt.close()
        else:
           plt.show()
    def printBing(self):
        a=[]
        for line in range(len(self.xList)):
            a.append(0)
        plt.pie(self.yList,a,self.xList,autopct='%1.1f%%')
        plt.show()
    def printRight(self,msg,x=False,y=False):
        self.xnote.append(self.xList[len(self.xList)-1]/100*50)
        minnum,maxnum=self.getminmax(self.yList);
        self.ynote.append(maxnum/100*75);
        self.note.append(msg);

    def getminmax(self,arr):
        min_res=float(arr[0])
        max_res=float(arr[0])
        for line in arr:
            if float(line)<min_res:
                min_res=float(line);
            if float(line)>max_res:
                max_res=float(line)
        return min_res,max_res

    def arrToString(self, arr, limit=5,str='\r\n'):
        if len(arr)<limit:
            length=len(arr);
        else:
            length=limit
        arr=str.join(arr[0:length])
        return arr