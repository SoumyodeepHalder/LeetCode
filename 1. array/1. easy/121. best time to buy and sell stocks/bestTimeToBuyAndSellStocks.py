class Solution(object):
    def maxProfit(self, prices):
        minSoFar=prices[0]
        maxProfit=0
        i=0
        pricesLen=len(prices)
        while i<pricesLen:
            if prices[i]<minSoFar:
                minSoFar=prices[i]
            elif prices[i]-minSoFar>maxProfit:
                maxProfit=prices[i]-minSoFar
            i+=1
        return maxProfit

if __name__=='__main__':
    obj=Solution()
    print(obj.maxProfit([2,5,1,6,4,7,3]))