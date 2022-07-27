import math

def speedMin(piles, time):
    print("now we are inside speedMIn func")
    i=0
    total=0
    while i != len(piles):
        print(total,"+", piles[i],end="=")
        total=total+piles[i]
        i=i+1
        print(total)
    print("now speedMin=",total,"/",time,"=",math.ceil(total/time))
    return math.ceil(total/time)

def eatingTime(piles, speed):
    i=0
    h=0
    while i != len(piles):
        recentPile=piles[i]
        
        if recentPile > speed:
            print("we're in recentPile>speed: hour=", h, "recentPile=", recentPile)
            h=h+int(recentPile/speed)
            recentPile=recentPile%speed
        
        if recentPile != 0:
            print("we're in recentpile !=0: hour=", h, "recentPile=", recentPile)
            recentPile = 0
            h = h+1
            i=i+1
        else:
            i=i+1
    return h
        


piles=[1000000000]
h=2
eatTime = h + 1
i=0
print("we are given piles=", piles, "time=",h)
print("firt we want to find minimum possible speed through speedMin func")
speed=speedMin(piles, h)
print("now we'll go inside while loop to count eating time for increasing speed")
while eatTime > h:
    print("lets try speed=",speed)
    eatTime=0
    eatTime=eatingTime(piles,speed)
    speed=speed+1
    print("eatTime=", eatTime)
print("speed required = ", speed-1)