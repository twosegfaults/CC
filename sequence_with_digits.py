def dig_split(num):
    digits = [int(i) for i in str(num)]
    return digits
def rec_fun(init, index):
    term=init
    for j in range(0, index-1):
        ld=dig_split(term)
        term+= (max(ld)*min(ld))
    return term
n = int(input())
for i in range(0, n):
    l1 = input().split()
    ans = rec_fun(int(l1[0]), int(l1[1]))
    print(ans)