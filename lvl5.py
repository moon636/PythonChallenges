def zap(list1,list2):
    zipped = []
    for i in list1:
        zipped.append((list1[i],list2[i]))
    print(zipped)

zap([0,1,2,3],[5,6,7,8])

