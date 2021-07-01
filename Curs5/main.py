from Fractie import Fractie


def main():
    x1 = int(input('Introdu numarator fractie 1: '))
    y1 = int(input('Introdu numitor fractie 1: '))

    x2 = int(input('Introdu numarator fractie 2: '))
    y2 = int(input('Introdu numitor fractie 2: '))

    fractie1 = Fractie(x1, y1)
    fractie2 = Fractie(x2, y2)

    print("Fractie 1:", fractie1)
    print("Fractie 2:", fractie2)

    print("Suma:", fractie1 + fractie2)
    print("Diferenta:", fractie1 - fractie2)

    print("Inversa fractie 1:", fractie1.inverse())

if __name__ == '__main__':
    main()