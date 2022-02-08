import platform
import math
from collections import Counter

x=platform.system()
print(x)
y= dir(platform)
print(y)
print(math.ceil(4.5))
x = Counter("helloworld")
for i in x.elements():
    print ( i, end = " ")
