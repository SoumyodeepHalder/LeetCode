class Solution:
    def twoSum(self, nums, target):
        i=0
        lenn=len(nums)
        while (i<lenn):
            j=i+1
            while (j<lenn):
                if nums[i]+nums[j]==target:
                    return [i,j]
                else:
                    j+=1
            i=i+1

if __name__=='__main__':
    obj = Solution()
    nums=[2, 7, 11, 15]
    target=18
    print(obj.twoSum(nums, target))