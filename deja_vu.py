n = int(input())
for i in range(0, n):
    l1 = input().split()
    l2 = input().split()
    l3 = input().split()
    a2 = [int(j) for j in l2]
    a3 = [int(k) for k in l3]
    max = 31
    for q in a3:
        if(max<=q): 
            continue
        for j in range(0, len(a2)):
            if (a2[j]%(pow(2, q)))==0:
                a2[j] += pow(2, (q-1))
        max = q
    print(*a2)