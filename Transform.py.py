import math

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

        def get_dimension(self):
            return self.__dimension

class Line(object):
    def __init__(self, line):
        try:
            if isinstance(line, tuple):
                if len(line) == 2:
                    if all(isinstance(element, Point) for element in line):
                        if len(set([point.get_dimension() for point in line])) == 1:
                            self.__start = line[0]
                            self.__end = line[1]
                        else:
                            raise DimError("Dimension Error: All the points must be of same dimension")
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
        except DimError as dim_exception:
            print(dim_exception)

        def length(self):
            return (sum([(a - b)**2 for a, b in zip(self.__start, self.__end)]))**(1/2)

        def slope(self):
            if self.length() != 0:
                return [((b - a) / self.length()) for a, b in zip(self.__start, self.__end)]
            else:
                return None

        def slope_angle(self, flag=False):
            if self.slope() is not None:
                if not flag:
                    return [(math.acos(cosine)) for cosine in self.slope()]
                else:
                    return [(math.degrees(math.acos(cosine))) for cosine in self.slope()]

class LineString(object):
    def __init__(self, lines):