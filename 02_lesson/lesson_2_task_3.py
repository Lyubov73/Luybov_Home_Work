import math
def square(side):
    are = side * side
    if not isinstance(side,int):
        are = math.ceil(are)
        return are
    print(square(4))
    print(square(4.6))
    print(square(5.9))