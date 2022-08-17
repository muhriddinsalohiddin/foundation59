"""
USHBU FILE DARS JARAYONIDA YOZILDI
"""
print("SALOM")


def Tubmi(son):
    if son < 2:
        return False
    for i in range(2,son//2):
        if son % i == 0:
            return False
    return True


for i in range(10):
    print(i)