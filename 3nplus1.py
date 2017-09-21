import time

boo = True
num = 0

print("This program takes a positive integer, and will multiply it by 3 and add 1 if it is odd, or will half it if it is even. \nThis is repeated until the final number is 1!")
time.sleep(3)
while boo or num <= 0:
    try:
        num = int(input('Enter a positive integer: '))
        boo = False
    except Exception as e:
        x = 0
print (num)

while num != 1:
    if num % 2 == 1:
        num = (num * 3)+1
    else:
        num = int(num/2)
    print (num)
