
def getRadix(x: int, result: int, index: int) -> int:
    tot = x
    for _ in range (index-1):
        tot = tot*x

    if tot == result:
        return x
    

    elif tot < result:
        return getRadix(x+1,result, index)

    else:
        return getRadix(x-1,result, index)

print(getRadix(12, 8, 3))



def getRadix(result: int, index: int) -> int:
    low = 1
    high = result

    while low <= high:
        mid = (low + high) // 2
        power = 1
        for _ in range(index):
            power *= mid

        if power == result:
            return mid
        elif power < result:
            low = mid + 1
        else:
            high = mid - 1

    return -1

