import string
v = int(input())
if v >= 1 and v <= 100:
    l = list()
    bl = string.ascii_uppercase[:]
    for i in range(v):
        l.append(input())
        for k in range(len(l[i])):
            if bl.count(l[i][k]) == 0:
                quit()
    yn = list()
    for il in l:
        if len(il) == 7:
            tin=['T','I','N','K','O','F','F']
            for j in range(len(il)):
                for t in range(len(tin)):
                    if il[j] == tin[t]:
                        tin.pop(t)
                        break
            if len(tin) == 0:
                yn.append("Yes")
            else:
                yn.append("No")
        else:
            yn.append("No")
    for y in yn:
        print(y)

