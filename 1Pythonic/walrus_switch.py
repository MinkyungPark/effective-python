# 가장 좋은 주스 먼저 제공하고, 바나나, 키위, 수박 제공
fresh_fruit = {
    "사과": 10,
    "바나나": 8,
    "레몬": 5,
}


def make_lemonade(count):
    n = 1
    print(f"레몬 {count*n} 개로 레모네이드 {count//n} 개를 만듭니다.")
    fresh_fruit["레몬"] -= count * n
    return f'레몬이 {fresh_fruit["레몬"]} 개 남았습니다.'


def out_of_stock():
    print(f"제료가 부족합니다. 재료를 보충해 주세요.")


def make_cider(count):
    n = 4

    print(f"사과 {count} 개로 사과주스 {count//n} 개를 만듭니다.")
    fresh_fruit["사과"] -= n * (count // n)
    return f'사과가 {fresh_fruit["사과"]} 개 남았습니다.'


def slice_bananas(count):
    print(f"바나나 {count} 개를 슬라이스합니다.")
    fresh_fruit["바나나"] -= count
    return count


class OutOfBananas(Exception):
    pass


def make_smoothies(count):
    n = 2
    if count > n:
        print(f"바나나 슬라이스 {count} 개로 스무디 {count//n} 개를 만듭니다.")
        return f'바나나가 {fresh_fruit["바나나"]} 개 남았습니다.'
    else:
        raise OutOfBananas


########### switch를 흉내내려면 if else elif를 깊게 내포시키는 것이다.
# 좋지 않다.
count = fresh_fruit.get("banana", 0)

if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get("사과", 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get("레몬", 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = "아무것도 없음"

# walrus를 이용하자
if (count := fresh_fruit.get("바나나", 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get("사과", 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get("레몬", 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = "아무것도 없음"