"""
BU FAQAT TEST UCHUN YOZILDI

from datetime import datetime

s = [int(input("Yilni kiriting:")),int(input("Oyni kiriting:")),int(input("kunn kiriting:"))]
d = [int(input("Yilni kiriting:")),int(input("Oyni kiriting:")),int(input("kunn kiriting:"))]

da = datetime(s[0],s[1],s[2])
da1 = datetime(d[0],d[1],d[2])
print(str(da-da1).split(" ")[0])
"""


s = "Two plus three is five"
lst = []
for i in s.split(' '):
    if len(i)>4:
        lst.append('*'*len(i))
        continue
    lst.append(i)
s = " ".join(lst)
print(s)