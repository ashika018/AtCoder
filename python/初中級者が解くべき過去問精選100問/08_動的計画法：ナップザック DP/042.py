# 動的計画法：ナップザックDP

city_num, trip_days = list(map(int, input().split(' ')))
city_distances = [int(input()) for _ in range(city_num)]
weathers_l = [int(input()) for _ in range(trip_days)]

memory_fields = [[10**8]*(trip_days+1) for _ in range(city_num+1)]

for day in range(trip_days+1):
    memory_fields[0][day] = 0

for city in range(city_num):
    for day in range(trip_days):
        memory_fields[city+1][day+1] = min(memory_fields[city+1][day], memory_fields[city][day]+city_distances[city]*weathers_l[day])

print(memory_fields[-1][-1])