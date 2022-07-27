s = "LVIII"
value=0
i=0
l=len(s)
while i<l:
    p=s[i]
    if p=="M":
        value+=1000
    elif p=="D":
        value+=500
    elif p=="L":
        value+=50
    elif p=="V":
        value+=5
    elif p=="C":
        if i==l-1:
            value+=100
        elif s[i+1]=="D":
            value+=400
            i+=1
        elif s[i+1]=="M":
            value+=900
            i+=1
        else:
            value+=100
    elif p=="X":
        if i==l-1:
            value+=10
        elif s[i+1]=="L":
            value+=40
            i+=1
        elif s[i+1]=="C":
            value+=90
            i+=1
        else:
            value+=10
    elif p=="I":
        if i==l-1:
            value+=1
        elif s[i+1]=="X":
            value+=9
            i+=1
        elif s[i+1]=="V":
            value+=4
            i+=1
        else:
            value+=1
    i+=1
print("value",value)