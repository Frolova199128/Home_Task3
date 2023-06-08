# Задача 20
# scrubble = {'A, E, I, O, U, L, N, S, T, R, А, В, У, И, Р, О, Р, С, Т' : 1, 'D, G, Д, К, Л, М, П, У' : 2, 'B, C, М, Р, Б, Г, Ё, Ь, Я' : 3, 'F, H, V, W, Y, Й, Ы' : 4, 'К, Ж, З, Ч, Ц, Ч' : 5, 'J, X, Ш, Э, Ю' : 8, 'Q, Z, Ф, Ш, Ъ' : 10}
# n = input("Введите слово заглавными буквами: ")
# score = 0
# for i in n:
#     for key in scrubble:
#         if i in key:
#             score += scrubble[key]
# print(score)

# Задача 16
# n = int(input("Введите количество элементов в массиве: "))
# array = [int(i) for i in input ("Ввведите значение элементов массива через пробел: ").split()]
# X = int(input("Введите число, которое необходимо найти: "))
# count = 0
# for element in array:
#     if element == X:
#         count +=1
# print(count)
          
# Задача 18
n = int(input("Введите количество элементов в массиве: "))
array = [int(i) for i in input ("Ввведите значение элементов массива через пробел: ").split()]
X = int(input("Введите число, ближайшее к которому необходимо найти: "))
count = abs(X - array[0])
num = array[0]
for element in range(1, n):
    m = abs(X - array[element])
    if count > m:
        count = m
        num = array[element]
print(num)