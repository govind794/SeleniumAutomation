# def insertionSort(n):
#     for i in range(len(n)):
#         key = n[i]
#         j = i - 1
#         while j >= 0 and n[j] > key:
#             n[j + 1] = n[j]
#             j = j - 1
#         n[j + 1] = key
#     return n
#
#
n = [5, 2, 4, 7, 6, 1, 8, 3, 9]
#
# print(insertionSort(n))

for i in range(len(n)):
    key = n[i]
    j = i - 1
    while j >= 0 and n[j] > key:
        n[j + 1] = n[j]
        j = j - 1
    n[j + 1] = key
print(n)
