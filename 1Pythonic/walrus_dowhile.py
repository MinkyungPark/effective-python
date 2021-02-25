# do while 없음
import random


def pick_fruit():
    if random.randint(1, 10) > 2:  # 80% 확률로 새 과일 보충
        return {
            "사과": random.randint(0, 10),
            "바나나": random.randint(0, 10),
            "레몬": random.randint(0, 10),
        }
    else:
        return None


def make_juice(fruit, count):
    if fruit == "사과":
        return [("사과주스", count / 4)]
    elif fruit == "바나나":
        return [("바나나스무디", count / 2)]
    elif fruit == "레몬":
        return [("레모네이드", count / 1)]
    else:
        return []


# 초기화하면서 pick_fruit() 호출, 마지막에 pick_fruit() 호출 2번 호출됨.
bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()

print(bottles)

# 무한 루프는 제어가 모두 break에 달려있어버림
bottles = []
while True:  # 무한루프
    fresh_fruit = pick_fruit()
    if not fresh_fruit:  # 중간에서 끝내기
        break

    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)

# walrus로 매번 fresh_fruit에 대입하고 검사할 수 있다.
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)