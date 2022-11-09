class Solution:
    @staticmethod
    def removeZeros(nums1):
        i=len(nums1)-1
        while 1:
            if nums1[i]==0:
                nums1.pop()
                print("nums1 index ",i,"found to be zero so it popped")
                print(nums1)
                i-=1
            else:
                break
        return nums1
    def merge(self, nums1,m,nums2,n):
        print("inside merge function")
        if n==0:
            print("n=0")
        elif m==0:
            print("m=0")
            nums1=nums2
            print("nums1=nums2")
        else:
            print("m and n both not equal to 0 so removing ending zeros")
            nums1=Solution.removeZeros(nums1)
            i=0
            j=0
            while i<n:
                print("loop started for nums2, current index ", i)
                while j<m and nums2[i]>nums1[j]:
                    print("loop started for nums1, current index ",j)
                    print("nums2[i]>nums1[j] is true")
                    j+=1
                print("loop ended for nums1")
                nums1.insert(j, nums2[i])
                m+=1
                print("inserted ", nums2[i], "at index", j)
                i+=1
                print(nums1)

if __name__=='__main__':
    nums1=[1,2,3,0,0,0]
    m=3
    nums2=[2,5,6]
    n=3
    print("nums1 =",nums1,"m =",m,"nums2 =",nums2,"n =",n)
    obj=Solution()
    obj.merge(nums1, m, nums2, n)