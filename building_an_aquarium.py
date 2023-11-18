x = int(input())
for a in range(0, x):
    l1 = input().split()
    l2 = input().split()
    array = [int(i) for i in l2]
    water_available = int(l1[1])
    max, min, temp= 10000000000, 1, 0
    while(max>min):
        water_used =0
        mid = min + (max-min)//2
        for i in range(0, int(l1[0])):
            if mid>array[i]:
                water_used += mid-array[i]
        if water_used>water_available:
            max = mid
        else:
            min = mid
        if(mid == temp):
            break
        temp = mid
    print(mid)