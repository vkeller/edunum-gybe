# Suite de Fibonacci
# Vincent Keller, 2023

borneSup = 100

fib = []
fib.append(0)
fib.append(1)
for i in range(2,borneSup,1):
    fib.append(0)

for i in range(2,borneSup,1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib)