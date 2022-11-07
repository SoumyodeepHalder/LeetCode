s='(){}}{'
i=0
arr=[]
lastElem=""
print("given string=",s)
while i<len(s):
    if s[i]=="(":
        print("detected (")
        arr.append("b1")
        i+=1
    elif s[i]=="{":
        print("detected {")
        arr.append("b2")
        i+=1
    elif s[i]=="[":
        print("detected [")
        arr.append("b3")
        i+=1
    elif s[i]==")":
        print("detected )")
        if lastElem=="b1":
            i+=1
            arr.pop(len(arr)-1)
        else:
            print("false")
            i=len(s)
    elif s[i]=="}":
        print("detected }")
        if lastElem=="b2":
            i+=1
            arr.pop(len(arr)-1)
        else:
            print("false")
            i=len(s)
    elif s[i]=="]":
        print("detected ]")
        if lastElem=="b3":
            i+=1
            arr.pop(len(arr)-1)
        else:
            print("false")
            i=len(s)
    if len(arr)==0 and i!=len(s):
        lastElem=""
        print("arr=",arr)
        print("lansElem=", lastElem)
    else:
        lastElem=arr[len(arr)-1]
        print("arr=",arr)
        print("lansElem=", lastElem)
if i!=len(s):
    if len(arr)!=0:
        print("false")
    else:
        print("true")