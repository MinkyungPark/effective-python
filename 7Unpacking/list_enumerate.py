snacks = [("베이컨", 350), ("도넛", 240), ("머핀", 180)]

# for idx, (val1, val2) in enumerate(list/tuple, start, end)
for rank, (name, cals) in enumerate(snacks, 1):
    print(f"#{rank}: {name} 은 {cals} 칼로리 입니다.")
