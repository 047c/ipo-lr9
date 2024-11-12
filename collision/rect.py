class RectCorrectError(Exception):
    pass
def isCorrectRect(spisok):
    kortezh1 = spisok[0]
    kortezh2 = spisok[1]
    if kortezh1[0] < kortezh2[0] and kortezh1[1] < kortezh2[1]:
        return True
    else:
        return False
