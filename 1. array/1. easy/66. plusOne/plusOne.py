class Solution:
    def findBreakingPoint(digit):
        digLen=len(digits)
        i=digLen-1
        while i>=0:
            if digits[i]==9:
                # print("digit ",i," = 9")
                i-=1
                continue
            else:
                # print("break point = ",i)
                break
        return i
    def convert9To0(i, digits):
        digLen=len(digits)
        while i<=digLen-1:
            digits[i]=0
            # print("digits ",i,"= 0")
            i+=1
        return digits
    @staticmethod
    def plusOne(digits):
        i=Solution.findBreakingPoint(digits)
        if i==-1:
            # print("all digits are 9")
            digits=Solution.convert9To0(0, digits)
            digits.insert(0, 1)
        else:
            digits[i]=digits[i]+1
            # print("digit ",digits[i]-1,"incremented to ", digits[i])
            i+=1
            digits=Solution.convert9To0(i, digits)
        return digits
if __name__=='__main__':
    digits=[8,9,9,9]
    print(Solution.plusOne(digits))
