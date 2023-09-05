def add_one(x):
    if x < 0:
        return x + 1
    else:
        return x - 1
    
#dis --- Python バイトコードの逆アセンブラ
import dis

dis.dis(add_one)
