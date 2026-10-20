Dorogi = [
    [0, 4, 0, 4, 0, 0, 0, 0],
    [4, 0, 4, 11, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 0, 0, 0],
    [4, 11, 4, 0, 7, 0, 0, 0],
    [0, 0, 0, 7, 0, 13, 0, 13],
    [0, 0, 0, 0, 13, 0, 13, 0],
    [0, 0, 0, 0, 0, 13, 0, 13],
    [0, 0, 0, 0, 13, 0, 13, 0]
]
count_vershin = 0
for i in Dorogi:
    count_vershin += 1
print("Количество вершин:", count_vershin)

total_sum = 0
for row in Dorogi:
    for value in row:
        total_sum += value

print("Сумма всех элементов матрицы:", total_sum)
num_reber = total_sum // 2
print("Количество рёбер:", num_reber)