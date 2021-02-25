# enumerate = lazy genrator

flavor_list = ["바닐라", "초콜렛", "피칸", "딸기"]
it = enumerate(flavor_list)
print(next(it))  # (0, '바닐라')
print(next(it))  # (1, '초콜렛')
print(next(it))  # (2, '피칸')

for idx, flavor in enumerate(flavor_list, 1):
    print(idx, flavor)