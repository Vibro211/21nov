from typing import List

array: List[str] = input("Введите массив строк через пробел: ").split(" ")
print(array)
L = len(array)
i = 0

while i <= L:
    if len(array[i]) > 3:
        array.pop(i)
    else:
        i += 1

print("Элементы этого массива из 3 и менее символов: ")
print(array)
