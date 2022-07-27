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

def lowestHighestIndexFinder(sumsArr):
    t=len(sumsArr)
    i=1
    lowestIndex=0
    highestIndex=0
    while i<t:
        if sumsArr[i]<sumsArr[lowestIndex]:
            lowestIndex=i
        elif sumsArr[i]>sumsArr[highestIndex]:
            highestIndex=i
        i+=1
    return [lowestIndex, highestIndex]

def arrIndexAdder(nums, lowestIndex, highestIndex):
    i=lowestIndex+1
    sum=0
    while i<=highestIndex:
        sum+=nums[i]
        i+=1
    return sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(nums)
if len(nums)==1:
    print(nums[0])
sumsArr=sumsArrayMaker(nums)
print(sumsArr)
lowestHighestIndex=lowestHighestIndexFinder(sumsArr)
print(lowestHighestIndex)
lowestIndex=lowestHighestIndex[0]
highestIndex=lowestHighestIndex[1]
if lowestIndex==0:
    if nums[0] > 0:
        lowestIndex=-1
greatestSum=arrIndexAdder(nums, lowestIndex, highestIndex)
print(greatestSum)