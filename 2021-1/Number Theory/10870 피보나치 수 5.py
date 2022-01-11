def fibonacci(k):
    if k<=1:
        return k
    return fibonacci(k-1)+fibonacci(k-2)

k=int(input())
print(fibonacci(k))