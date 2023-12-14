class Point(object):
    def __init__(self, arg):
        try:
            if isinstance(arg, tuple):
                if all(isinstance(element, (int, float)) for element in arg):
                    if len(arg) <= 3 and len(arg) > 0:
                        self.__dimension = len(arg)
                        self.__point = arg
                    else:
                        raise DimError("Dimension Error: Expected maximum 3 dimensions")
                else:
                    raise TypeError("Type Error: Expected <float/int>")
            else:
                raise ArgumentError("Argument Error: Expected <tuple>")
        except TypeError as type_exception:
            print(type_exception)

class Line(object):
    def __init__(self, line):
        try:
            if isinstance(line, tuple):
                if len(line) == 2:
                    if all(isinstance(element, Point) for element in line):
                        self.__start = line[0]
                        self.__end = line[1]
                    else:
                        raise TypeError("Type Error: Expected pair of Points")
                else:
                    raise SizeError("Size Error: Expected one pair of Points")
            else:
                raise TypeError("Argument Error: Expected <tuple>")
        except TypeError as type_exception:
            print(type_exception)
        except SizeError as size_exception:
            print(size_exception)