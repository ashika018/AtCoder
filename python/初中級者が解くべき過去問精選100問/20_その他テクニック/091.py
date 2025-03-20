# その他テクニック（単純な幾何計算）
import math
a, b, x = list(map(int, input().split(' ')))

# 分子：numerator, 分母：denominator
if(x<(a**2)*b/2):
    numerator, denominator = b, 2*x/(a*b)
else:
    numerator, denominator = 2*b-(2*x/a**2), a
ans = math.degrees(math.atan(numerator/denominator))
print(ans)
