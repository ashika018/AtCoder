# 全探索：ビット全探索

# スイッチのon, offのパターンは高々、2**N < 2**10通りである
# また、これはbit全探索をすることで、もれなく簡単に全パターンを列挙することができる
# 各パターンのスイッチに対して、すべての電球がonになるかどうかを試していく。

num_switches, num_lights = list(map(int, input().split(' ')))
conection_l = [list(map(int, input().split(' '))) for _ in range(num_lights)]
numbers_for_check = list(map(int, input().split(' ')))

# あるライトのon, offを判断
def light_on_or_off(connection_info, light_index):
    on_light_count = 0
    for swich in connection_info[1:]:
        on_light_count += int(bit[swich-1])
    if(on_light_count%2==numbers_for_check[light_index]): return 'on'
    else: return 'off'

# （2**スイッチの数）分のon, offの組み合わせが存在
ans = 0
for i in range(2**num_switches):
    lights_state = []
    bit = [(i>>j)&1 for j in range(num_switches)]
    for k, connection_info in enumerate(conection_l):
        lights_state.append(light_on_or_off(connection_info, k))
    if(set(lights_state)==set(['on'])): ans += 1

print(ans)