import math

while True:
    try:
        d, vf, vg = map(int, input().split())
        tempo_ladrao = 12 / vf
        dist_guarda = math.sqrt(12**2 + d**2)

        tempo_guarda = dist_guarda / vg
        if tempo_guarda <= tempo_ladrao:
            print('S')
        else:
            print('N')

    except EOFError:
        break