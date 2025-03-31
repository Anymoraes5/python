t = int(input())

nh = 0 
m = t // 60
if m > 60:
    nh = m // 60
nm = m % 60
h = ((t % 60) // 60 ) + nh
s = t % 60

print(f'{h}:{nm}:{s}')