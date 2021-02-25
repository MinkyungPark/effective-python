# assert는 타입 validate 용으로 쓰임?
# '예외 처리'대신 '가정 설정문'
# assert 조건, '메세지'
# 메세지는 생략 가능


def assert_test(t):
    assert type(t) is int, "정수 아닌 값이 있네"


lists = [1, 3, 2.3]
for i in lists:
    assert_test(i)

# AssertionError: 정수 아닌 값이 있네