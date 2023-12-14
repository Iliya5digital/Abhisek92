import re

class Solution(object):
    def __init__(self):
        self.pattern = re.compile(r"^(M*)((CM)|(CD)|(DC{0,3})|(C{0,3}))((XC)|(XL)|(LX{0,3})|(X{0,3}))((IX)|(IV)|(VI{0,3})|(I{0,3}))$")

    def romanToInt(self, s):
        groups = re.search(self.pattern, s).groups()
        m = 1000 * len(groups[0])

        c1 = 900 if groups[2] else 0
        c2 = 400 if groups[3] else 0
        c3 = 500 + (100 * (len(groups[4]) - 1)) if groups[4] else 0
        c4 = 100 * len(groups[5]) if groups[5] else 0

        x1 = 90 if groups[7] else 0
        x2 = 40 if groups[8] else 0
        x3 = 50 + (10 * (len(groups[9]) - 1)) if groups[9] else 0
        x4 = 10 * len(groups[10]) if groups[10] else 0

        v1 = 9 if groups[12] else 0
        v2 = 4 if groups[13] else 0
        v3 = 5 + (len(groups[14]) - 1) if groups[14] else 0
        v4 = len(groups[15]) if groups[15] else 0

        return m + c1 + c2 + c3 + c4 + x1 + x2 + x3 + x4 + v1 + v2 + v3 + v4
