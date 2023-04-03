fib =lambda x: x if x <= 1 else fib(x-1)+fib(x-2)
print([fib(i) for i in range(10)])

