def is_prime(number):
    divs = [i for i in range(1, number + 1) if number % i == 0]
    return True if len(divs) == 2 else False


def average(*args):
    return sum(args) / len(args)
