# 二分探索

# この場合、計算し始めるまでの年数をxとすると、コスト = x + P / (2**(x/1.5))となる。
# この関数は単調ではないので、直接、二分探索を使うことはできない。
# しかし、極値を一つしか持たない関数なので、三文探索をすることで、最小値を求めることができる

P = float(input())

def cost(x):
    return x + P * pow(2, -(x/1.5))

# 三分探索の実装
# left, right間を3分割していき2/3ずつ下位の候補の範囲を絞っていく
# numの値が大きければ大きいほど、精度は向上していく
def ternary_search(left, right, num):
    for i in range(num):
        m1 = (2*left + right)/3
        m2 = (left + 2*right)/3
        # cost(m1) < cost(m2)ならば、最小値を取るxは必ずleft~m2の間にある
        # 逆にいうと、m2~right間に解は絶対にない
        if(cost(m1) < cost(m2)): right = m2
        else: left = m1  # cost(m1)>cost(m2)ならば、costを最小にするxは、left~m1間には存在しない
    
    if(cost(m1) < cost(m2)): return cost(m1)
    else: return cost(m2)


print(ternary_search(0, 10**18, 10**5))