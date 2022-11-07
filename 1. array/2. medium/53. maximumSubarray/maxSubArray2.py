def sumsArrayMaker(nums):
    t=len(nums)
    i=0
    value=0
    sumsArr=[]
    while i<t:
        value+=nums[i]
        sumsArr.append(value)
        i+=1
    return sumsArr

def highestIndexFinder(sumsArr):
    t=len(sumsArr)
    i=1
    highestIndex=0
    while i<t:
        if sumsArr[i]>sumsArr[highestIndex]:
            highestIndex=i
        i+=1
    return highestIndex
def lowestIndexFinder(sumsArr, highestIndex):
    i=1
    lowestIndex=0
    while i<highestIndex:
        if sumsArr[i]<sumsArr[lowestIndex]:
            lowestIndex=i
        i+=1
    return lowestIndex

def arrIndexAdder(nums, lowestIndex, highestIndex):
    i=lowestIndex+1
    sum=0
    while i<=highestIndex:
        sum+=nums[i]
        i+=1
    return sum

nums = [-2,-1]
print(nums)
if len(nums)==1:
    print(nums[0])
sumsArr=sumsArrayMaker(nums)
print(sumsArr)
highestIndex=highestIndexFinder(sumsArr)
lowestIndex=lowestIndexFinder(sumsArr, highestIndex)
if lowestIndex==0:
    if nums[0] > 0:
        lowestIndex=-1
print("index=",lowestIndex, highestIndex)
greatestSum=arrIndexAdder(nums, lowestIndex, highestIndex)
print(greatestSum)