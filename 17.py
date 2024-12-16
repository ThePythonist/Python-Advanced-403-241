def myhash(x):
    if len(str(x)) == 1:
        return x
    else:
        digits = []
        for i in str(x):
            digits.append(int(i))

        return myhash(sum(digits))


print(myhash(93))
