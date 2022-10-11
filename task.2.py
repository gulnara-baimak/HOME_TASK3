#<Задание 2>
#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16]
#[2, 3, 5, 6] => [12, 15]

from random import randint

Num = int(input('Введите размер списка: '))
list = []
list2 = []

for i in range(Num):
    list.append(randint(0, 9)) #определяем рандомно диапазон чисел от 0 до 9 в нашем листе

for i in range(len(list)): 
    while i < len(list)/2 and Num > len(list)/2:
        Num = Num - 1
        a = list[i] * list[Num]
        list2.append(a)
        i += 1

print(f'Первоначальный список: {list}')
print(f'Полученный список: {list2}')

# my_list = [2, 3, 4, 5, 6]
# result_list = []
# for i in range((len(my_list)+1)//2):
#     result_list.append(my_list[i]*my_list[len(my_list)-1-i])
# print(result_list)
