x=[9, 6, 7, 1, 2]
for i in range(1, len(x)):
    j = i
    while (j > 0) and (x[j - 1] > x[j]):
        tmp = x[j]
        x[j] = x[j - 1]
        x[j - 1] = tmp
        j = j - 1
        # print(x)
print(x)
