key = "my_key"
value = 1.2345

formatted = f"{key} = {value}"  # my_key = 1.2345
print(formatted)

formatted = f"{key!r:<10} = {value:.2f}"  # 'my_key'   = 1.23
print(formatted)

places = 3
number = 1.23445
print(f"내가 고른 숫자는 {number:.{places}f}")

t = ("Hi, I am", "song", 123)
print(f"tuple: {t}")

s = "arrange"
print(f"{s:<10}")  # 왼쪽 정렬
print(f"{s:^10}")  # 가운데 정렬
print(f"{s:>10}")  # 오른쪽 정렬
print(f"{{{s}}}, {{s}}")  # {'arrange'}, {s}

dic = {"name": "apple", "num": 3}  # dictionary
print(f'name {dic["name"]} has {dic["num"]}')

n = [100, 200, 300]  # list
print(f"list : {n[0]}, {n[1]}, {n[2]}")
for v in n:
    print(f"list with for : {v}")


import datetime

date = datetime.datetime.now()
print(f"{date:%Y-%m-%d} is on a {date:%A}")
