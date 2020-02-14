import fibonach

print(fibonach.my_add(3,8))

# (f_n)^2 + (f_{n+1}^2 = f_{2n+1}

n = 5

print(fibonach.fib_num_l(n)**2 + fibonach.fib_num_l(n+1)**2)
print(fibonach.fib_num_l(2*n+1))