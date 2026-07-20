x = 11

def test(x):
    if x<0:
        return False
    if x<10:
        return True
    if x%10 == 0:
        return False
    newX = 0
    while newX < x:
        tempx = x%10
        newX = newX * 10 + tempx
        x //= 10

    if newX == x or newX/10 == x:
        return True
    else:
        return False

print(test(11))