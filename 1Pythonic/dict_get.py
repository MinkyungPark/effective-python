from urllib.parse import parse_qs

my_values = parse_qs("빨강=5&초록=0&파랑=", keep_blank_values=True)

print(my_values)  # {'빨강': ['5'], '초록': ['0'], '파랑': ['']}

# 값이 비어있거나 없는 경우 0으로 default 생성해주기

# dic.get(key, default) key가 없는 경우 default로 저장
# or -> False면 좌 값 아니면 우 값
# 빈 문자열, 리스트, 0 모두 암시적으로 False 취급.
red = my_values.get("빨강", [""])[0] or 0
print(f"빨강: {red!r}")
green = my_values.get("초록", [""])[0] or 0
print(f"초록: {green!r}")
blue = my_values.get("파랑", [""])[0] or 0
print(f"파랑: {blue!r}")