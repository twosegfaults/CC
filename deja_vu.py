n = int(input())
for i in range(0, n):
    l1 = input().split()
    l2 = input().split()
    l3 = input().split()
    a2 = [int(j) for j in l2]
    a3 = [int(k) for k in l3]
    m = 31
    for q in a3:
        if(m<=q): 
            continue
        for j in range(0, len(a2)):
            if (a2[j]%(pow(2, q)))==0:
                a2[j] += pow(2, (q-1))
        m = q
    print(*a2)