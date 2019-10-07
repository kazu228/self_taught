# *args
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9,))
print(sum(2, 5, 6))

# **kwargs

def  bar(**kwargs):
    for x in kwargs:
        print(x)
        print(kwargs[x])
    print(kwargs)

bar(x=10, y=20, z="Python")