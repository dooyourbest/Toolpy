from filedeal import FileDeal
def count():
	file=FileDeal();
	file.load('./line_road.txt');
	list = file.getRow()
	allrow=file.getCol(list,2,',');
	ret,mapnum = count.changenum(ret,lisan)
    res=count.countList(ret)
    xlist,ylist,xdot,ydot,dotstr=count.returnXY(res,dotnum)
    num,index,msgold=count.countpersen(xlist,ylist,limitPersent,mapnum)#百分比mapnum

