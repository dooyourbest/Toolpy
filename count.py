#!/usr/bin/env python
# coding=utf-8
from  sklearn import preprocessing
class Count:
    def __init__(self):
      pass
      #统计数组的数目，用int统计
    def countList(self,arr):
        allDict={}
        for line in arr:
            line =int(float(line))
            if line in allDict:
                allDict[line]=allDict[line]+1
            else:
                allDict[line]=1
        return allDict
     #f返回会xlist,ylist，xdot,ydot,dotnum
    def returnXY(self,dict,dotnum,tuple=False):
        xlist=[]
        ylist=[]
        xdot=[]
        ydot=[]
        dotstr=[]
        keymax=max(dict)
        keymim=min(dict)
        if tuple !=False:
            if keymax>tuple[1]:
                keymax=tuple[1];
            if keymim<tuple[0]:
                keymim=tuple[0]
        for i in range(keymim,keymax+1):
            try:
                ylist.append(dict[i])
                xlist.append(i)
                if dict[i]>dotnum:
                    xdot.append(i);
                    ydot.append(dict[i])
                    dotstr.append(str(i)+','+str(dict[i]))
            except:
                pass
        return xlist,ylist,xdot,ydot,dotstr

    def lisan(self,arr,start=0,end=100):
        tmp=[];
        for line in arr:
            tmp.append([line])
        minMaxScale=preprocessing.MinMaxScaler(copy=True,feature_range=(start,end))
        minMax=minMaxScale.fit_transform(tmp)
        tmp=[]
        for line in minMax:
            tmp.append(line[0])
        return tmp
    #改变数组的去边，统一离散在一个范围内
    def changenum(self,arr,allInterval=100):
        minnum,maxnum=self.getminmax(arr)
        limit=float(maxnum)/allInterval;
        tmp=[]
        for line in arr:
            res=float(line)/limit
            if int(res)==0 and res>0:
                res=1
            tmp.append(res);
        return tmp,limit;

    def getminmax(self,arr):
        min_res=float(arr[0])
        max_res=float(arr[0])
        for line in arr:
            if float(line)<min_res:
                min_res=float(line);
            if float(line)>max_res:
                max_res=float(line)
        return min_res,max_res
   #计算每个到分数段的分数占比
    def countpersen(self,xarr,yarr,limit,mapnum):
        allNum=0
        tmpNum=0
        a=0
        msg=[]
        for line in yarr:
             allNum=int(line)+allNum

        for i in range(len(xarr)):
            tmpNum=tmpNum+int(yarr[i])
            persend=float(tmpNum)/float(allNum)
            msg.append(str(persend)+'--'+str(xarr[i])+'--'+str(xarr[i]*mapnum))
            if persend>limit:
                 if a==0: 
                    a=xarr[i]*mapnum;
                    index=i
        
        return a,index,msg
    #计算饼图的需要的值
    def countBing(self,xarr,yarr,limit=0.01):
        allNum=self.getArrAllNumber(yarr)
        x_tmp=[]
        y_tmp=[]
        other=0
        for i in range(len(yarr)):
            persent=float(yarr[i])/allNum
            if persent>limit:
                x_tmp.append(xarr[i]);
                y_tmp.append(yarr[i]);
            else :
                other=other+yarr[i];
        y_tmp.append(other)
        x_tmp.append('other')
        return x_tmp,y_tmp
    def getArrAllNumber(self,arr):
        num=0
        for line in arr:
            num=float(line)+num
        return num



    def dictChange(self, adict,doctnum,tumple=False): 
        keys = adict.keys() 
        keys.sort()
        tmp={}
        x=[]
        y=[]
        xdot=[]
        ydot=[]
        dotstr=[]
        if tumple == False:
            for line in keys:
                x.append(line)
                y.append(adict[line])
                if adict[line]>doctnum:
                    xdot.append(line);
                    ydot.append(adict[line])
                    dotstr.append(str(line)+','+str(adict[line]))
            return x,y,xdot,ydot,dotstr
        else:
            minnum=tumple[0]
            maxnum=tumple[1]
            for line in keys:
                if line>minnum and line<maxnum:
                    x.append(line)
                    y.append(adict[line])
                    if adict[line]>doctnum:

                        xdot.append(line);
                        ydot.append(adict[line])
                        dotstr.append(str(line)+','+str(adict[line]))
            return x,y,xdot,ydot,dotstr
    def getcacluate(self,x,y):
        allNum=self.getArrAllNumber(y);
        minnum,maxnum=self.getminmax(x);
        print maxnum;
        tmp_number=0
        all_arr=[]
        count=[0.75,0.80,0.85,0.90,0.95,0.99];
        countDict={}
        for line in range(len(x)):
            tmp_number=tmp_number+y[line]
            persent=tmp_number/allNum
            for i in range(len(count)):
                if persent>count[i] and count[i] not in countDict:
                    # print str(x[line])+'--'+str(tmp_number)+'--'+str(persent);
                    countDict[count[i]]=str(x[line])+'--'+str(tmp_number)+'--'+str(persent);
                    all_arr.append(str(x[line])+'--'+str(tmp_number)+'--'+str(persent))
        return all_arr;
