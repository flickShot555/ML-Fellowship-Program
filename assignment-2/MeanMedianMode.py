def mean_Calc(myNums):
    mySum=sum(myNums)
    count = len(myNums)
    return mySum/count

def median_Calc(myNums):
    myNums.sort()
    count = len(myNums)
    if count % 2 == 0:
        mid = count // 2
        return (myNums[mid-1] + myNums[mid]) / 2
    else:
        mid = count // 2
        return myNums[mid]
    
def mode_Calc(myNums):
    myNums.sort()
    count = len(myNums)
    maximumCount = 0
    mode = myNums[0] #myNums=[1,3,2,4,3,4,3,4,1], count=9
    i = 0
    while i < count:
        thisNum = myNums[i]
        thisCount = myNums.count(thisNum)
        if thisCount > maximumCount:
            maximumCount = thisCount
            mode = thisNum
        i += thisCount
    return mode