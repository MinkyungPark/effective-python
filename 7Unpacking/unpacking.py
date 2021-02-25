## 추천하는 방법은 아니지만 이처럼 작성이 가능하다
favorite_snacks = {"짠 과자": ("프레즐", 100), "단 과자": ("쿠키", 180), "채소": ("당근", 20)}

(
    (type1, (name1, cals1)),
    (type2, (name2, cals2)),
    (type3, (name2, cals3)),
) = favorite_snacks.items()

print(f"내가 좋아하는 과자 중에 {type1}은 {name1}이 있고 칼로리는 {cals1}임.")