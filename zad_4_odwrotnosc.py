import zad_3_iloczyn as z3


def inverse(x):
    b = x
    i = 13
    const = 1
    if x == '00':
        return 'nie istnieje'
    while i > 0:
        if int(bin(i),2) & int(bin(const),2) == 1:
            tmp = b
        else:
            tmp = x
        b = z3.multiply(b, tmp)
        i = i - 1
    return b


if __name__ == '__main__':
    yd = inverse('f1')
    print("Odwrotność: ", yd)