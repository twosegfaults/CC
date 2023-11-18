x = int(input())
for i in range(0, x):
    inp = int(input())
    arr =[0, 0, 0, 0]
    i = 3
    for j in range(1, 5):
        arr[i]= inp%10
        if (arr[i]==0):
            arr[i]=10
        inp= inp//10
        i-=1
    move_time =0
    init = arr[0]-1
    for k in range(0, 3):
        diff = abs(arr[k+1]-arr[k])
        move_time+= diff
    print(move_time+4+init)