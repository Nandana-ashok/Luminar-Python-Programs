num = int(input('enter the number :'))
temp = num
total = 0
length = len(str(num))

while num>0:
    n = num % 10
    total += n ** length
    num //= 10
if temp == total:
    print(f'{temp} is an armstrong number')
else:
    print(f'{temp} is not an armstrong number')
