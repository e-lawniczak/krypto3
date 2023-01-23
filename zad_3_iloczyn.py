import main as m
import zad_1_suma as z1
import zad_2_xtime as z2


def binary_product(x, y):
    solve = '00'
    x = m.hex_to_bin(x)
    x = str(x)[2:]

    length = len(x)
    length2 = len(x) - 1
    for i in range(length):
        if x[i] == '1':
            tmp = y
            counter = length2
            while counter != 0:
                tmp = z2.binary_xtime(tmp)
                counter = counter - 1
            solve = z1.binary_sum(tmp, solve)
        length2 -= 1
    return solve


if __name__ == '__main__':
    product = binary_product('f1', '12')
    print("Iloczyn: ", product)