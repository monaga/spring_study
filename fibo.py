fibo_num = input('入力 :')
print('出力：', fibo_num)
a = int(fibo_num)
x = [0, 1]
for i in range(a - 2):
     com = x[i] + x[i + 1]
     x.append(fibo_num)
print(x)
