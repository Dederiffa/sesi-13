import math

def hitung_bola(radius):
    volume = (4/3) * math.pi * radius**3
    luas_permukaan = 4 * math.pi * radius**2
    return volume, luas_permukaan