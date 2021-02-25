# 서로소 검사
# for/while 뒤에 else 쓰지 X
a, b = 4, 9
for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print("서로소 아님")
        break  # else 실행되지 않음
else:
    print("서로소임")

# 1. 도우미 함수를 작성해 바로 리턴
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


assert coprime(a, b)
assert not coprime(3, 6)

# 2. 도우미 함수를 작성해 변수 리턴
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime


assert coprime_alternate(a, b)
assert not coprime_alternate(3, 6)