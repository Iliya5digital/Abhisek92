import struct

def sqrt(x):
    x = float(x)
    y = struct.pack('>f', x)
    i = struct.unpack('>i', y)[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.pack('>i', i)
    z = struct.unpack('>f', y)[0]
    z = z * (1.5 - 0.5 * x * z * z)
    return 1 / z # return round(1/z) for closest int

