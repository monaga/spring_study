com = input('入力 :')
print('出力：', com)
a = int(com)
x = [0, 1]
for i in range(a - 2):
     com = x[i] + x[i + 1]
     x.append(com)
print(x)
