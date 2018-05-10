def fun(n):
    val = [1, 2, 5, 10]
    f = [0 for i in range(101)]
    f[0] = 1
    for i in range(4):
        for j in range(val[i], 100 + 1, val[i]):
            f[j] = f[j] + f[j - val[i]]
    return f[n]


print(fun(5))
