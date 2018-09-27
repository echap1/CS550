import sys

fib = [1, 1]

for i in range(sys.argv - 2):
    fib += [fib[i] + fib[i + 1]]

print(", ".join(str(x) for x in fib))