from zad_1_suma import binary_sum
from zad_2_xtime import xtime
from zad_3_iloczyn import multiply
from zad_4_odwrotnosc import inverse

if __name__ == '__main__':
    # x = "FF"
    # y = "10"

    x = "FF"
    y = "FF"

    # x = "AB"
    # y = "CD"

    # x = "01"
    # y = "A2"

    x = "23"
    y = "F1"

    # x = "02"
    # y = "02"

    suma = binary_sum(x, y)
    przesuniecie = xtime(x)
    iloczyn = multiply(x, y)
    inversja = inverse(x)
    print(
        """
        x: {}
        y: {}
        add: {}
        xtime (x): {}
        multiply: {}
        inwersja: {}
        """.format(x, y, suma, przesuniecie, iloczyn, inversja)
    )
