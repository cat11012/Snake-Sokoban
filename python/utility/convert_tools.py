import math

def surface_size_ratio(x: int, y: int) -> tuple[int, int]:
    gcd = math.gcd(x, y)
    return (x/gcd, y/gcd)

