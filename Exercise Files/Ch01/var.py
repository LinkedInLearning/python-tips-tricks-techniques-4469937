#代入
x = 1
y = 2
print(x, y)

#1行で代入
x, y = 10, 20
print(x, y)

#他の言語で一般的な値の入替え
tmp = x
x = y
y = tmp
print(x, y)

#1行で書ける
x, y = y, x
print(x, y)

#何が起こっているかと言うと
x, y = (y, x)
print(x, y)