class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            print("numRow = 1, return [[1]]")
            return [1]
        elif rowIndex==1:
            print("numRow = 2, return [[1],[1,1]]")
            return [1,1]
        prevArr=[1,1]
        print("prevArr set to [1,1]")
        prevArrLen=2
        i=0
        while rowIndex>1:
            print("loop started to generate new row")
            currentArr=[1]
            print("currentArr set to [1]")
            while i<prevArrLen-1:
                currentArr.append(prevArr[i]+prevArr[i+1])
                print("loop started to generate new elem in currentArr, current index = ",i)
                print("currentArr upgrated to ",currentArr)
                i+=1
            currentArr.append(1)
            print("appeded final 1")
            print("currentArr upgrated to ",currentArr)
            prevArr=currentArr
            prevArrLen+=1
            rowIndex-=1
            i=0
        return currentArr


if __name__=='__main__':
    obj=Solution()
    print(obj.getRow(int(input("enter row index: "))))