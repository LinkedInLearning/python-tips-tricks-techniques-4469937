lst_a = [1,2,3,4,5,]
lst_b = lst_a
lst_b[0] = 10
print(lst_b)
print(lst_a)

print(id(lst_a))
print(id(lst_b))

# #listのcopyメソッド
lst_a = [1,2,3,4,5,]
lst_b = lst_a.copy()
lst_b[0] = 10
print(lst_b)
print(lst_a)

print(id(lst_a))
print(id(lst_b))
