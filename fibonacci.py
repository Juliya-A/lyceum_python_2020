int x = 1 #число в ряду Фиббоначи с позицией 1
int y = 2 #число в ряду Фиббоначи с позицией 2
n = input("Введите позицию числа из ряда Фиббоначи")

fib (n, x, y)
 if n==0
 return 0
 elif n==1
 return 1
 elif n==2
 return 1

else:
return fib(n-1) + fib(n-2)
