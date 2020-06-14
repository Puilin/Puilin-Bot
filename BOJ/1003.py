n = int(input())

def fib(n):    
    global zero_count
    global one_count
    if n <= 1:
        if n == 0:
            zero_count += 1
            return n
        else:
            one_count += 1
            return n
    else:
        return fib(n-1) + fib(n-2)

zero_count, one_count = 0, 0
_ = fib(n)
print(zero_count, one_count)