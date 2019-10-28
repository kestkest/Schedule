import sys

x1, v1, x2, v2 = [int(i) for i in sys.argv[1:]]


def will_they_meet():
    if x1 == x2 and v1 == v2:
        print('YES')
    elif x1 <= x2 and v1 <= v2:
        print('NO')
    elif x1 >= x2 and v1 >= v2:
        print('NO')
    else:
        if (x1 - x2) % (v2 - v1) == 0:
            print('YES')
        else:
            print('NO')


will_they_meet()
