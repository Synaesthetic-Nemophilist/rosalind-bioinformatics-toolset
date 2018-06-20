def generalized_fibonacci(data):
    data = data.split()

    epochs = int(data[0])

    rate = int(data[1])

    pairs = fib_gen(epochs, rate)

    return str(pairs)


def fib_gen(n, k):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib_gen(n - 1, k) + fib_gen(n - 2, k) * k
