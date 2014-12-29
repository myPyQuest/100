""" find cost of tile
    to cover  W x H floor
"""

costToCover = lambda w, h, ppm: str(w * h * ppm) + ' $.'
print(costToCover(int(input('ширина (м): ')), int(input('длинна (м): ')), int(input('цена за квадрат($): '))))