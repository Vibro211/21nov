from typing import List

A = input("Введите массив строк через пробел: ").rstrip()
A = A.split(" ")
print(A)
B = []

for i in A:
    if len(i) <= 3:
        B.append(i)





print("Элементы этого массива из 3 и менее символов: ")
print(B)
