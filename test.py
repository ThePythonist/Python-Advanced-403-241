# def func(*args):
#     args = list(args)
#     print(args)
#     print(type(args))
#
#
# func(256, 128, 512)


def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))

    for i in kwargs.values():
        print(i)


func(name="adv-403-241", teacher="sadeghi", students=["ali", "fateme", "amir"])
