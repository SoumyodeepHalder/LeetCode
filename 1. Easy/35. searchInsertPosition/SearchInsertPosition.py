nums=[1,3,5,6]
target=4
i=0
l=len(nums)
if nums[l-1]<target:
    print(l)
else:
    while i<l and nums[i]<target:
        i+=1
    print(i)