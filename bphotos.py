import sys
order = sys.stdin.readlines()
flag =0
for i in order:
    if i== order[0]:
        continue
    else:
        color= i.strip()
        clr = color.replace(" ", "")
        for j in clr:
            if(j=='B' or j=='W' or j=='G'):
                continue
            else:
                flag=1
                break
if flag==0:
    print("#Black&White")
else: print("#Color")