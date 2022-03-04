def fibo(x):
    a = 0
    b = 1
    print(0)
    print(1)
    for i in range(2, x):
        result = a + b
        a = b
        b = result
        print(result)
fibo(10)


def fibo(num):
    a = 0
    b = 1
    if (num == 1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, num):
            result = a + b
            a = b
            b = result
            print(result)
fibo(20)
