import sys
L= sys.stdin.readlines()
for i in L:
    if i==L[0]:
        continue
    else:
        word=i.strip()
        if len(word)>10:
            print(word[0], len(word)-2, word[len(word)-1], sep='')
        else: print(word)