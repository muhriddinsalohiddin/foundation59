"""
USHBU FILE DARS JARAYONIDA YOZILDI
"""
def Tubmi(son):
    if son < 2:
        return False
    for i in range(2,son//2):
        if son % i == 0:
            return False
    return True