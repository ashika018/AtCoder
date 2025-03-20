# 数学的な問題

takahashi_cookies, aoki_cookies, K = list(map(int, input().split(' ')))

if(K<=takahashi_cookies):
    print(f'{takahashi_cookies-K} {aoki_cookies}')
elif(K<=takahashi_cookies+aoki_cookies):
    print(f'{0} {aoki_cookies+takahashi_cookies-K}')
else:
    print(f'{0} {0}')