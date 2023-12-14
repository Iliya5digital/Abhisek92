class ArgumentTypeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))


def gcd(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            if b > a:
                a, b = b, a
            if b == 0:
                raise ValueError("Illegal value Zero(0): Expected non zero integers")
            else:
                if a % b == 0:
                    return b
                else:
                    return gcd((a % b), b)
        else:
            raise ArgumentTypeError("Invalid Argument Type: Expected <int int>")
    except ArgumentTypeError as arg_exception:
        print str(arg_exception)
        return None
    except ValueError as val_exception:
        print str(val_exception)
        return None


def lcm(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            if gcd(a, b) == 1:
                return a*b
            else:
                return (a * b) / gcd(a, b)
        else:
            raise ArgumentTypeError("Invalid Argument Type: Expected <int int>")
    except ArgumentTypeError as arg_exception:
        print str(arg_exception)
        return None
    except ValueError as val_exception:
        print str(val_exception)
        return None


class Fraction:
    __sign = None
    __numerator = None
    __denominator = None

    def get_numerator(self):
        return self.__numerator


    def get_denominator(self):
        return self.__denominator


    def get_sign(self):
        return self.__sign


    def __init__(self, a, b):
        try:
            if (isinstance(a, int) or isinstance(a, float) or isinstance(a, Fraction)) and (isinstance(b, int) or isinstance(b, float) or isinstance(b, Fraction)):
               if isinstance(b, int) and b == 0:
                   raise ValueError("Illegal value Zero(0): Expected non zero integers")
               if (isinstance(a, float) or isinstance(b, float)) or (isinstance(a, Fraction) or isinstance(b, Fraction)) :
                   if isinstance(a, float):
                       frac = a.as_integer_ratio()
                       a = Fraction(frac[0], frac[1])
                   if isinstance(b, float):
                       frac = b.as_integer_ratio()
                       b = Fraction(frac[0], frac[1])
                   c = a.__div__(b)
                   self.__numerator = c.get_numerator()
                   self.__denominator = c.get_denominator()
               else:
                   self.__numerator = abs(a)
                   self.__denominator = abs(b)
               if a*b < 0:
                   self.__sign = -1
               else:
                   self.__sign = 1
            else:
                raise ArgumentTypeError("Invalid Argument Type: Expected <int/Fraction, int/Fraction>")
        except ArgumentTypeError as arg_exception:
            print str(arg_exception)
        except ValueError as val_exception:
            print str(val_exception)


    def __str__(self):
        if (self.__sign is not None) and (self.__numerator is not None) and (self.__denominator is not None):
            if self.get_denominator() == 1:
                return str(self.__sign * self.__numerator)
            else:
                return str(self.__sign * self.__numerator) + "/" + str(self.__denominator)
        else:
            return None


    def inverse(self):
        a = self.__denominator
        b = self.__numerator
        c = Fraction(a, b)
        return c.simplify()


    def simplify(self):
        factor = gcd(self.__numerator, self.__denominator)
        if factor is not None:
            a = self.__numerator / factor
            b = self.__denominator / factor
            return Fraction((self.__sign * a), b)
        else:
            return None


    def __add__(self, fraction):
        try:
            if isinstance(fraction, Fraction) or isinstance(fraction, int) or isinstance(fraction, float):
                if isinstance(fraction, int):
                    fraction = Fraction(fraction, 1)
                if isinstance(fraction, float):
                    frac = a.as_integer_ratio()
                    fraction = Fraction(frac[0], frac[1])
                b = self.__denominator * fraction.get_denominator()
                a = (self.__sign * (b / self.__denominator) * self.__numerator) + (self.__sign * (b / fraction.get_denominator()) * fraction.get_numerator())
                return Fraction(a, b).simplify()
            else:
                raise ArgumentTypeError("Invalid Argument Type: Expected <int/Fraction>")
        except ArgumentTypeError as arg_exception:
            print str(arg_exception)


    def __sub__(self, fraction):
        try:
            if isinstance(fraction, Fraction) or isinstance(fraction, int) or isinstance(fraction, float):
                if isinstance(fraction, int):
                    fraction = Fraction(fraction, 1)
                if isinstance(fraction, float):
                    frac = a.as_integer_ratio()
                    fraction = Fraction(frac[0], frac[1])
                b = self.get_denominator() * fraction.get_denominator()
                a = (self.get_sign() * (b / self.get_denominator()) * self.get_numerator()) - (self.get_sign() * (b / fraction.get_denominator()) * fraction.get_numerator())
                return Fraction(a, b).simplify()
            else:
                raise ArgumentTypeError("Invalid Argument Type: Expected <int/Fraction>")
        except ArgumentTypeError as arg_exception:
            print str(arg_exception)


    def __mul__(self, fraction):
        try:
            if isinstance(fraction, Fraction) or isinstance(fraction, int) or isinstance(fraction, float):
                if isinstance(fraction, int):
                    fraction = Fraction(fraction, 1)
                if isinstance(fraction, float):
                    frac = a.as_integer_ratio()
                    fraction = Fraction(frac[0], frac[1])
                a = self.__numerator * fraction.__numerator
                b = self.__denominator * fraction.__denominator
                return Fraction(a, b).simplify()
            else:
                raise ArgumentTypeError("Invalid Argument Type: Expected <int/Fraction>")
        except ArgumentTypeError as arg_exception:
            print str(arg_exception)


    def __div__(self, fraction):
        try:
            if isinstance(fraction, Fraction) or isinstance(fraction, int) or isinstance(fraction, float):
                if isinstance(fraction, int):
                    if fraction == 0:
                        raise ValueError("Illegal value Zero(0): Expected non zero integers")
                    else:
                        fraction = Fraction(fraction, 1)
                if isinstance(fraction, float):
                    if fraction == 0.0:
                        raise ValueError("Illegal value Zero(0): Expected non zero integers")
                    else:
                        frac = a.as_integer_ratio()
                        fraction = Fraction(frac[0], frac[1])
                return (self.__mul__(fraction.inverse())).simplify()
            else:
                raise ArgumentTypeError("Invalid Argument Type: Expected <int/Fraction>")
        except ArgumentTypeError as arg_exception:
            print str(arg_exception)
        except ValueError as val_exception:
            print str(val_exception)