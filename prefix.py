strs = ["ab","a"]
i = 0
j = 0
print("given strs=",strs)
str = ""
if len(strs) == 1:
    print("length of strs is 1 so prefix=", strs[0])
    j=200
while i<len(strs)-1:
    if len(strs[i]) == 0:
        print("a blank string detected at", i,"so prefix is a blank string")
        j=200
    i+=1
i=0
while j < 200:
    while i < len(strs) - 1:
        if len(strs[i])==j:
            j=200
            break
        elif len(strs[i+1])==j:
            j=200
            break
        elif strs[i][j] == strs[i + 1][j]:
            print("strs",i,j,"=","strs",i+1,j,"=",strs[i][j])
            i += 1
        else:
            print("an unmatch detected so the final prefix", str)
            j=200
            break
    if j < 200:    
        str += strs[i][j]
        print("prefix now = ", str)
    i = 0
    j += 1
print("final prefix=",str)