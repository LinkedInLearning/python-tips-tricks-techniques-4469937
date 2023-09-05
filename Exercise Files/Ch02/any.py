nums = [0, 0, 0, 0, 0,]
print(any(nums))

def not_black(rgb):
    for val in rgb:
        if 0 < val:
            return True
    return False

print(not_black([0, 0, 0]))
print(not_black([0, 10, 0]))

def not_black(rgb):
                #内包表記
    return any(0 < val for val in rgb)

print(not_black([0, 0, 0]))
print(not_black([0, 10, 0]))