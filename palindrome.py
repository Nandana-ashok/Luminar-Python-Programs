num = 121221
l = len(str(num))
temp = num
pal = 0

while num > 0 :
    n = num % 10
    pal = pal * 10 + n
    num //= 10

if temp == pal:
    print(f'{temp} is a palindrome number')
else:
    print(f'{temp} is not a palindrome number')