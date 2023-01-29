

def binary_sum(x, y):
    sum = int(x, base=16) ^ int(y, base=16)
    return str(hex(sum)).upper()[2:]

if __name__ == '__main__':
    sum = binary_sum('AE', '11')
    print("Suma: ", sum)