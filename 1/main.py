array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]


def count_sheeps(sheep):
    arr = []
    a = (i for i in range(len(sheep)))
    for i in a:
        if sheep[i]:
            arr.append(sheep[i])
    return len(arr)


print(count_sheeps(array1))


def count_sheeps_2(x):
    return x.count(True)


print(count_sheeps_2(array1))
