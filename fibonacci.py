a = int(input("Введите порядковый номер числа Фиббоначи: "))

def fib(a):
    if a==1 or a==2:
        return 1
    else:
        return fib(a-2) + fib(a-1)
print(fib(a))
