def power(x, y):
    res = 1

    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x)

        y = y >> 1 # y = y/2
        x = (x*x)

    return res

if __name__ == "__main__":
    print (power(5,4))
