def multiplier():
    num = 1
    while True:
        yield num
        num *= 2


gen = multiplier()
print(next(gen))  # 输出 1
print(next(gen))  # 输出 2
print(next(gen))  # 输出 4
print(next(gen))  # 输出 8
print(next(gen))  # 输出 8
print(next(gen))  # 输出 8
print(next(gen))  # 输出 8
print(next(gen))  # 输出 8
