def fibonacci(n):
    temp = [0] * (n + 1)
    temp[0], temp[1] = 0, 1
    for i in range(2, n + 1):
        temp[i] = temp[i - 1] + temp[i - 2]
    return temp[n]


if __name__ == '__main__':
    print(fibonacci(5))
