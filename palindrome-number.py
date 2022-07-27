def arrayify(x):
    arr = []
    while x != 0:
        arr.append(x % 10)
        x = int(x / 10)
    return arr


def numberify(arr):
    i = 0
    num = 0
    while i != len(arr):
        z = len(arr) - i - 1
        num = num + arr[i] * 10 ** z
        i = i + 1
    return num


x = 121
print("input number is",x)
if x < 0:
    print("not a palindrome")
else:
    arr = arrayify(x)
    num = numberify(arr)
    if x == num:
        print("its a palindrome number")
    else:
        print("not a palindrome number")
