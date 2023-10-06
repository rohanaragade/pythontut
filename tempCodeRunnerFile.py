def sexi(n):
    return lambda a: a*n

mydoubler=sexi(2)
print(mydoubler(11))