# def product(args):
#     prod = [[]]
#     for arg in args:
#         prod = [x + [y] for x in prod for y in arg]
#
#     return prod
#


def product(args):
    prod = [[]]
    for arg in args:
        prod = [x + [y] for x in prod for y in arg]
    return prod

a = [[1, 2, 3], [1,2],[True,False]]
print(product(a))