_ = input()
wardrobe = {
    '0': 0,
    '1': 0,
    '2': 0
}
clothes_list = input().split()
for item in clothes_list:
    wardrobe[item] = wardrobe.get(item, 0) + 1
for key, value in wardrobe.items():
    print((key + ' ') * value, end='')
