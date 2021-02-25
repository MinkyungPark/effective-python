from urllib.parse import parse_qs

my_values = parse_qs("빨강=5&초록=0&파랑=", keep_blank_values=True)

red = my_values.get("빨강", [""])[0] or 0
print(f"빨강: {red!r}")
green = my_values.get("초록", [""])[0] or 0
print(f"초록: {green!r}")
blue = my_values.get("파랑", [""])[0] or 0
print(f"파랑: {blue!r}")

# 값을 int로 바꿔야할 때
red = int(my_values.get("빨강", [""])[0] or 0)
# 복잡한 식을 한줄로 표현 X
red_str = my_values.get("빨강", [""])[0] or 0
red = int(red_str[0]) if red_str[0] else 0
# 여러 줄로 나누어쓴 if else 문이 더 정확하다
red_str = my_values.get("빨강", [""])[0] or 0
if red_str[0]:
    red = int(red_str[0])
else:
    red = 0

# 도우미 함수를 쓰자 단지 2,3 번 반복에 불과하더라도
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default