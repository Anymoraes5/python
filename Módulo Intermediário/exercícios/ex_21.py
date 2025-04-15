x = int(input())

for i in range(x):
    count = 0
    y = float(input())

    while y > 1:
        y = y / 2
        count += 1
    print(f'{count} dias')