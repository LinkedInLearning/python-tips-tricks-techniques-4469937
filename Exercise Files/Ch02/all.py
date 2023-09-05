nums = [10, 2, 4, 1, 8,]
print(all(nums))

def valid_rgb(rgb):
    for val in rgb:
        if not 0 <= val <= 255:
            return False
    return True

print(valid_rgb([255, 255, 255]))
print(valid_rgb([290, 100, 200]))

def valid_rgb(rgb):
                #内包表記
    return all(0 <= val <= 255 for val in rgb)

print(valid_rgb([255, 255, 255]))
print(valid_rgb([290, 100, 200]))