def func1(x):
    x += 10
    return x


def func2(lis):
    lis.append(3)
    return lis


x = 1
print(func1(x))  # 11
print(x)  # 1

lis = [1, 2]
print(func2(lis))  # [1,2,3]
print(lis)  # [1,2,3]
