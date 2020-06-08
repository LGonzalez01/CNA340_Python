def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return 0
    elif a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a+b+c

a1 = int(input())
b1 = int(input())
c1 = int(input())
print(lone_sum(a1, b1, c1))