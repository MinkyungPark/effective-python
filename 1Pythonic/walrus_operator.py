# 0인지 검사하는 패턴 파이썬에서 자주 사용
def make_lemonade(count):
    pass


def out_of_stock():
    pass


fresh_fruit = {"사과": 10, "배": 9, "바나나": 6}
count = fresh_fruit.get("레몬", 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

# walrus operator = assignment expression 대입식
# count가 if에만 영향을 준다는 것을 파악하기 쉽다.
# 대입식은 대입문이 쓰일 수 없는 곳에도 쓸 수 있게 해줌.
if count := fresh_fruit.get("레몬", 0):
    make_lemonade(count)
else:
    out_of_stock()

# 레몬은 0인지 아닌지만 검사하면 된다
# 사과일 경우 4개 이상이 있는지 검사해야한다면
if (count := fresh_fruit.get("사과", 0)) > 4:
    make_lemonade(count)
else:
    out_of_stock


## 바나나 스무디 바나나2개 필요하고 없을 경우 OutOfBananas 발생
def slice_banana(count):
    return count * 3


class OutOfBananas(Exception):
    pass


def make_smooth(count):
    return "smoothie"


pieces = 0
count = fresh_fruit.get("바나나", 0)
if count >= 2:
    pieces = slice_banana(count)

try:
    smoothies = make_smooth(pieces)
except OutOfBananas:
    out_of_stock()

# walrus
pieces = 0
if (count := fresh_fruit.get("바나나", 0)) >= 2:
    pieces = slice_banana(count)

try:
    smoothies = make_smooth(pieces)
except OutOfBananas:
    out_of_stock()