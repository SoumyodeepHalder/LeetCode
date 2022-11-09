class Solution(object):
    def generate(self, numRow):
        if numRow==1:
            print("numRow = 1, return [[1]]")
            return [[1]]
        elif numRow==2:
            print("numRow = 2, return [[1],[1,1]]")
            return [[1],[1,1]]
        prevArr=[1,1]
        print("prevArr set to [1,1]")
        prevArrLen=2
        finalArr=[[1],[1,1]]
        print("finalArr set to [[1],[1,1]]")
        i=0
        while numRow>2:
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
            finalArr.append(currentArr)
            print("finalArr upgrated to ",finalArr)
            prevArr=currentArr
            prevArrLen+=1
            numRow-=1
            i=0
        return finalArr

if __name__=='__main__':
    obj=Solution()
    print(obj.generate(int(input("How many rows to generate\n"))))
