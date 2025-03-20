



def C():
    N, M = map(int, input().split())
    taka = [[0]*N]*N
    aoki = [[0]*N]*N
    """
    for i in range(N):
        taka = taka.append([])
        aoki = aoki.append([])
        for j in range(N):
            taka[i].append(0)
            aoki[i].append(0)
    """
    #print(taka)
    #print(aoki)
    for k in range(1,2*M+1):
        a, b = map(int, input().split())
        #print(a, b)
        if(k<M+1):
            taka[a-1][b-1] = 1
            taka[b-1][a-1] = 1
            print(taka)
        else:
            aoki[a-1][b-1] = 1
            aoki[b-1][a-1] = 1

    jis_t, jis_a = [], []
    print(taka)
    print(aoki)
    for i in range(N):
        j_p_t, j_p_a = 0, 0
        for j in range(N):
            j_p_t += taka[i][j]
            j_p_a += aoki[i][j]
        jis_t.append(j_p_t)
        jis_a.append(j_p_a)

    print(jis_a)
    print(jis_t)
    if(jis_t.sort()!=jis_a.sort()): return "No"

    jis_tl, jis_al = [], []
    for i in range(N):
        jis_tl_i, jis_al_i = [], []
        for j in range(N):
            if(taka[i][j]==0 and aoki[i][j]==0):
                jis_tl_i.append(0)
                jis_al_i.append(0)
            elif(taka[i][j]==1 and aoki[i][j]==0):
                jis_tl_i.append(jis_t[j])
                jis_al_i.append(0)
            elif(taka[i][j]==0 and aoki[i][j]==1):
                jis_tl_i.append(0)
                jis_al_i.append(jis_a[j])
            else:
                jis_tl_i.append(jis_t[j])
                jis_al_i.append(jis_a[j])
        jis_tl.append(jis_tl_i)
        jis_al.append(jis_al_i)
    for i in range(N):
        jis_al[i].sort()
        jis_tl[i].sort()
    if(sorted(jis_al, reverse=True, key=lambda x: x[0])==sorted(jis_tl, reverse=True, key=lambda x: x[0])): return "Yes"
    else: return "No"


print(C())