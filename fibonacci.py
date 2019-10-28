x = int(input("Please enter the last value in the fibonacci sequence that you want to show: "))


def fibo(n):
    a = 0
    b = 1
    if n < 0:
        print("Invalid number!")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        # 2 elements are printed so 0 and 1 are already occupied now from index 2 start
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if c > 500:
                break
            print(c)


fibo(x)
