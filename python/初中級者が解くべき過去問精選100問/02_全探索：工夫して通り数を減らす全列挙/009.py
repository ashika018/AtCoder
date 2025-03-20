# 全探索：工夫して通り数を減らす全列挙

# まず、見つけたい星座の点の中から、基準点を一つ選び、基準点から残りのm-1点へのベクトルを計算し、set型Aに変換
# 次に写真に写っているn個のなかに、必ず基準点があるはずなので、
# 各点に対して、ベクトルを計算し、set型Bに変換。AがBの部分集合となっているかどうかの全探索を行う。

m = int(input())
sign_location_l = [list(map(int, input().split(' '))) for _ in range(m)]
n = int(input())
stars_location_l = [list(map(int, input().split(' '))) for _ in range(n)]

base_point = sign_location_l[0]
base_x = base_point[0]
base_y = base_point[1]
vectors_from_basepoint = set(['('+','.join([str(point[0]-base_x), str(point[1]-base_y)])+')' for point in sign_location_l])
# print(vectors_form_basepoint)

for candidate_point in stars_location_l:
    candidate_x, candidate_y = candidate_point[0], candidate_point[1]
    vectors_form_candidatepoint = set(['('+','.join([str(point[0]-candidate_x), str(point[1]-candidate_y)])+')' for point in stars_location_l])
    if(vectors_from_basepoint <= vectors_form_candidatepoint): break

print(f'{candidate_x-base_x} {candidate_y-base_y}')
