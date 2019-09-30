# 1

def square(a):
    """
    params: int
    返り値：引数の2乗
    """
    return print(a ** 2)

square(2)

# 2

def print_make(b):
    """
    params: str
    戻り値：　引数の出力
    """
    b = str(b)
    return print(b)

print_make("Hello Python")

# 3

def five(c, d, e, f=4, g=5): 
    """
    params: int
    戻り値： 5つの引数の合計値
    """
    return print(c+d+e+f+g)

five(1,2,3)

# 4

def sub(h):
    """
    params: int
    戻り値：　引数の割る2
    """
    result = h // 2
    return result

def four_cal(i):
    """
    params: int
    戻り値：　引数の掛ける4
    """
    cal = i * 4
    return print(i)

num = sub(4)
four_cal(num)
# 5

def change_float(j):
    """
    params: float
    戻り値：　引数の出力
    """
    try:
        k = float(j)
        return print(k)
    except ValueError:
        return print("Invalid input.")

change_float("Hello")
change_float("123")
change_float(123)
change_float(True)   # 1.0
change_float(False)  #0.0
change_float("55.0")