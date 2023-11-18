n= int(input())
for i in range (0, n):
    l = input().split()
    chest = int(l[0])
    key = int(l[1])
    stamina = int(l[2])
    if key<=chest:
        print(chest)
    else:
        if(stamina<=key-chest):
            print(chest+ stamina + 2*(key-chest-stamina))
        else: print(key)