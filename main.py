#2
# quantity = int(input())
# coordinates_list = []
# for i in range(quantity):
#     coordinates = input().replace(' ', '')
#     coordinates = tuple(coordinates)
#     coordinates_list.append(coordinates)
# print(coordinates_list)

#3
# replacement_dict = {
#     'к': 'т',
#     'р': 'а',
#     'и': 'к',
#     'в': 'л',
#     'о': 'у',
#     'я': 'ч',
#     'з': 'ш',
#     'ы': 'е'
# }
#
# input_text = input("Введите текст на старом алфавите: ")
#
# result_text = ""
#
# for char in input_text:
#     if char in replacement_dict:
#         result_text += replacement_dict[char]
#     else:
#         result_text += char
#
# print("Текст на новом алфавите:", result_text)

#4
# list_of_sets = []
# number_of_students = int(input())
# number_of_essays = int(input())
# for num in range(number_of_students):
#     essays = input().split()
#     list_of_sets.append(set(essays))
# if list_of_sets:
#     similarities = set.intersection(*list_of_sets)
#     print(similarities)
# else:
#     print('aghh')
# print(list_of_sets)

#5
# quantity_of_exams = input()
# for i in range(quantity_of_exams):
#     x = input()
#     y = input()
#     z = input()
#     number_exam = input()

#1
# def determine_winner(n, k, chizhik_weights, pyzhik_weights, ksenia_weights):
#     # Сортируем массивы с весами грибов
#     chizhik_weights.sort()
#     pyzhik_weights.sort()
#     ksenia_weights.sort()
#
#     # Находим k-ый по величине гриб (k-1, так как индексация с 0)
#     chizhik_k = chizhik_weights[k - 1]
#     pyzhik_k = pyzhik_weights[k - 1]
#     ksenia_k = ksenia_weights[k - 1]
#
#     # Определяем победителя
#     if chizhik_k > pyzhik_k and chizhik_k > ksenia_k:
#         return "Чижик"
#     elif pyzhik_k > chizhik_k and pyzhik_k > ksenia_k:
#         return "Пыжик"
#     elif ksenia_k > chizhik_k and ksenia_k > pyzhik_k:
#         return "Ксюша"
#     else:
#         return "Ничья"
#
#
# # Чтение входных данных
# n = int(input())
# k = int(input())
# chizhik_weights = list(map(int, input().split()))
# pyzhik_weights = list(map(int, input().split()))
# ksenia_weights = list(map(int, input().split()))
#
# # Определение победителя
# result = determine_winner(n, k, chizhik_weights, pyzhik_weights, ksenia_weights)
# print(result)

#5
# def remove_duplicates(n, deliveries):
#     students = {}
#
#     for delivery in deliveries:
#         x, y, z, k = delivery
#         coordinates = (x, y, z)
#
#         if coordinates not in students:
#             students[coordinates] = set()
#
#         students[coordinates].add(k)
#
#     return students
#
#
# # Чтение входных данных
# n = int(input())
# deliveries = [tuple(map(int, input().split())) for _ in range(n)]
#
# # Удаление дубликатов и получение результата
# students = remove_duplicates(n, deliveries)
#
# # Вывод результата
# for coordinates, works in students.items():
#     print(*coordinates, *sorted(works))

