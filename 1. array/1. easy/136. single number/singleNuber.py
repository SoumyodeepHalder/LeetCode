class Solution(object):
    def findNum(self, nums):
        i=0
        numsLen=len(nums)
        if numsLen==1:
            print("numsLen = 1, so returning nums[i]")
            return nums[i]
        nums.sort()
        print("nums sorted")
        print(nums)
        while i<numsLen:
            if i<numsLen-1 and nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]

if __name__=='__main__':
    obj=Solution()
    print(obj.findNum([2,1,2,1,4]))