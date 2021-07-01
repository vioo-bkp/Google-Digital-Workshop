def sum(*args, **kwargs):
    sum = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            sum += arg
    return sum

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

def sum_odd(n):
    if n == 0:
        return 0
    return n + sum_odd(n - 1) if n % 2 == 1 else sum_odd(n - 1)

def sum_even(n):
    if n == 0:
        return 0
    return n + sum_even(n - 1) if n % 2 == 0 else sum_even(n - 1)

def read_int():
    n = input()
    try:
        n = int(n)
    except ValueError:
        n = 0
    return n

def main():
    print(sum(1, 5, -3, 'abc', [12, 56, 'cad']))
    print(sum())
    print(sum(2, 4, 'abc', param_1=2))

    print(sum_n(5))
    print(sum_odd(5))
    print(sum_even(5))

    print(read_int())

if __name__ == '__main__':
    main()
    