case = int(input())

leds = {
    '1' : 2,
    '2' : 5,
    '3' : 5,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 3,
    '8' : 7,
    '9' : 6,
    '0' : 6,
}

for i in range(case):
    led = input()
    total = 0
    for l in led:
        if l in leds:
            total += leds[l]
    print(f'{total} leds')
    
