import helper as m
import zad_1_suma as z1


def xtime(x):
    x = str(m.hex_to_bin(x))
    x = str(x)[2:]
    B1 = '00011011'
    B1 = hex(int(B1, 2))

    length = len(x)
    while length < 8:
        x = '0' + x
        length = length + 1
    if x[0] == '1':
        x = x[1:8] + '0'
        x = hex(int(x, 2))
        return z1.binary_sum(x, B1)
    elif x[0] == '0':
        x = x[1:8] + '0'
        return hex(int(x, 2))


if __name__ == '__main__':
    xd = xtime('a1')
    print("Xtime: ", xd)