class RectCorrectError(Exception):
    pass
def isCorrectRect(spisok):
    kortezh1 = spisok[0]
    kortezh2 = spisok[1]
    if kortezh1[0] < kortezh2[0] and kortezh1[1] < kortezh2[1]:
        return True
    else:
        return False
def isCollisionRect(spisok1, spisok2):
    if not isCorrectRect(spisok1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(spisok2):
        raise RectCorrectError("2й прямоугольник некорректный")
    kortezh1 = spisok1[0]
    kortezh2 = spisok1[1]
    kortezh3 = spisok2[0]
    kortezh4 = spisok2[1]
    x_1_minimalny = kortezh1[0]
    y_1_minimalny = kortezh1[1]
    x_1_maksimalny = kortezh2[0]
    y_1_maksimalny = kortezh2[1]
    x_2_minimalny = kortezh3[0]
    y_2_minimalny = kortezh3[1]
    x_2_maksimalny = kortezh4[0]
    y_2_maksimalny = kortezh4[1]
    if x_1_maksimalny < x_2_minimalny or x_1_minimalny > x_2_maksimalny or y_1_maksimalny < y_2_minimalny or y_1_minimalny > y_2_maksimalny:
        return False
    else:
        return True
def intersectionAreaRect(spisok1, spisok2):
    if not isCorrectRect(spisok1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(spisok2):
        raise RectCorrectError("2й прямоугольник некорректный")
    kortezh1 = spisok1[0]
    kortezh2 = spisok1[1]
    kortezh3 = spisok2[0]
    kortezh4 = spisok2[1]
    x_1_minimalny = kortezh1[0]
    y_1_minimalny = kortezh1[1]
    x_1_maksimalny = kortezh2[0]
    y_1_maksimalny = kortezh2[1]
    x_2_minimalny = kortezh3[0]
    y_2_minimalny = kortezh3[1]
    x_2_maksimalny = kortezh4[0]
    y_2_maksimalny = kortezh4[1]
    if isCollisionRect(spisok1, spisok2):
        dlina = min(x_1_maksimalny, x_2_maksimalny) - max(x_1_minimalny, x_2_minimalny)
        shirina = min(y_1_maksimalny, y_2_maksimalny) - max(y_1_minimalny, y_2_minimalny)
        return dlina * shirina
    else:
        return 0