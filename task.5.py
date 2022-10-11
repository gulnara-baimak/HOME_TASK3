#<Задание 5>
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

def Fib1(k):
    if k in [1, 2]:                       
        return 1
    else:
        return Fib1(k-1) + Fib1(k-2)

def Fib2(k):
    if k == 1:                       
        return 1
    elif k == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, k):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
myInt = int(input('Введите число: '))
for n in range(1, myInt + 1):
    list.append(Fib1(n))
    list.insert(0, Fib2(n))
print(list)
