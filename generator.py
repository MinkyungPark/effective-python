def test_generator():
    yield 1
    yield 2
    yield 3


print(next(test_generator()))  # 1
print(next(test_generator()))  # 1
print(next(test_generator()))  # 1

gen = test_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
