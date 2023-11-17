n = int(input('Введите число: '))
num1 = 0
num2 = 1
for i in range(n):
    num2 = num1 + num2
    num1 = num2 - num1
print(num1)
