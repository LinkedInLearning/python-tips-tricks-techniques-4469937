import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 実行開始: {datetime.datetime.now()}")

        # デコレートする関数の呼び出し
        ret = func(*args, **kwargs)

        print(f"{func.__name__} 実行終了: {datetime.datetime.now()}")

        return ret
    return wrapper

@logger
def greet(name):
    return(f"Hello {name}!")

print(greet("ガニエブさん"))

@logger
def accum(max):
    accum_sum = 0 
    for i in range(1,max+1):
        accum_sum += i
    
    return(accum_sum)

a = accum(100000)
print(a)