num_months = int(input())
num_days_l = input().split(' ')
num_days_l = [int(i) for i in num_days_l]

one_year_days = sum(num_days_l)
goal = (one_year_days+1)/2

for month in range(1, num_months+1):
    days = num_days_l[month-1]
    if(goal <= days): 
        print(f'{month} {int(goal)}')
        break
    else: goal -= days