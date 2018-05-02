#!/usr/bin/env python
# coding=utf-8
from  count import Count
from plant import Plot
from word import Word
from filedeal import FileDeal
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
def countXY(feature_num):
    lisan=1000 #离散区间
    dotnum=500 #打点人数
    limitPersent=0.99;
    count=Count()
    file=FileDeal();
    file.load('./line_road.txt');
    list = file.getRow()
    allrow=file.getCol(list,feature_num+1,',');
    # ret,mapnum = count.changenum(allrow,lisan)
    # ret=count.lisan(ret,0,100000);
    res=count.countList(allrow)
    # res=count.sortedDictValues(res);
    xlist,ylist,xdot,ydot,dotstr=count.dictChange(res,dotnum)
    msg=count.getcacluate(xlist,ylist);
    # xlist,ylist,xdot,ydot,dotstr=count.returnXY(res,dotnum)

    # print xlist,ylist;
    # num,index,msgold=count.countpersen(xlist,ylist,limitPersent,mapnum)#百分比mapnum
    plot=Plot();
    # msg=msgold
    # msg.insert(0,'limit'+str(limitPersent)+'--'+str(index)+'--'+str(num))
    # msg=plot.arrToString(msgold)
    plot.setXY(xlist,ylist)
    name='feature_'+str(feature_num)
    plot.setTitle(name)
    plot.setdot(xdot,ydot,dotstr);
    # plot.printRight(msg)
    """
    print '=============='+name
    print xlist
    print ylist
    print xdot
    print ydot
    print dotstr
    # """
    # plot.printZhexian();
    # pictureName='./picture3/'+name+'.png'
    # plot.printZhexian(True,pictureName);
    # plot=Plot();
    # xlist,ylist=count.countBing(xlist,ylist)
    # plot.setXY(xlist,yalist)
    # plot.printBing()
    # """
    # return msg,pictureName;

# word=Word()
allFeature="'导航里程','导航时间','gps点个数','偏航gps点个数','超速次数','急转弯次数','急加速次数','急减速次数','无路网次数','白天占比','夜晚占比','高峰期占比','100km', '10km', '1km', '200km', '200m', '300km', '30km', '3km', '400km', '500km', '500m', '50km', '5km', 'g500km','-10', '-20', '-2~2', '-50', '-80', '10', '100', '20', '50', '80', 'g100','里程','绑路点数','限速等级6','限速等级7','限速等级4','限速等级5','限速等级2','限速等级3','限速等级1','限速等级8','车道数个数为1的','车道数个数为2','车道数个数为3',' 经过的高架路的个数','经过的跨线天桥个数','经过地道的个数','导航次数'";
allFeature=allFeature.split(',')
# isDebug=False
for  i in range(1,55):
    # try:
    # print i
    # exit()
        # word.addHeading(allFeature[i-1].decode('utf8').strip())
        print allFeature[i-1].decode('utf8').strip()+'---------------------------'
    # if isDebug:
        # res,picturePath=countXY(i)
        countXY(i)

        # word.addPicture(picturePath)
        # print(res);

        # word.addTable(res,'--')
    # else:
        # try:
            # res,picturePath=countXY(i)
            # word.addPicture(picturePath)
            # word.addTable(res,'--')
        # except:
            # pass


    # except:
    #     pass
# word.save('特征分布非离散2.docx')



