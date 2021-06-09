def front_back(str):
    if len(str)==0:
        return str
    else:
        l = []
        for i in str:
            l.append(i)
        var1= l[0]
        var2= l[-1]
        l[0]= var2
        l[-1]= var1
        a=''
        for k in l:
            a= a+k
        return a
print(front_back('abtahee'))