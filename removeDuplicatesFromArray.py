i=0
pop=0
nums=[1,1,2,2]
while i<len(nums)-1:
    if nums[i]==nums[i+1]:
        nums.pop(i)
        pop+=1
    else:
        i+=1
k=i+1
i=0
while i<pop:
    nums.append(0)
    i+=1

print("final",nums,k)