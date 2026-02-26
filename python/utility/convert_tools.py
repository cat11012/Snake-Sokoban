import math

def surface_size_ratio(x: int, y: int) -> tuple[int, int]:
    gcd = math.gcd(x, y)
    return (x/gcd, y/gcd)

def find_available_screen_ratio(ratio: tuple[int, int]) -> tuple[int, int]:
    """
    background images x-axis lcm: 336

    below are the y-axis values for each screen size ratio when the x-axis is 336:
    3x2: 224
    4x3: 252
    16x9: 189
    16x10: 210
    21x9: 144
    """
    multiple = 336 / ratio[0]
    y = ratio[1] * multiple

    if y > 238:
        return (4, 3)
    elif y > 217:
        return (3, 2)
    elif y > 199:
        return (16, 10)
    elif y > 167:
        return (16, 9)
    else:
        return (21, 9)

def find_screen_size(screen_size: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    """(window_size, screen_ratio)"""
    screen_ratio = surface_size_ratio(screen_size[0], screen_size[1])

    if (screen_ratio in ((3,2), (4,3), (16,9), (16,10), (21,9))):
        return (
            (int(screen_size[0]/1.2), int(screen_size[1]/1.2)),
            screen_ratio
        )
    
    new_screen_ratio = find_available_screen_ratio(screen_ratio)
    len1 = screen_size[0] / 1.2
    len2 = screen_size[1] / 1.2 / new_screen_ratio[1] * new_screen_ratio[0]
    length = min(len1, len2)
    return (
        (int(length), int(length / new_screen_ratio[0] * new_screen_ratio[1])),
        new_screen_ratio
    )

