list = [2, 5, 6, 8, 13, 42, 50, 53, 62, 66, 70, 80, 89, 90]

keresett = 70
also = 0
felso = len(list) - 1

while also <= felso:
    k = (felso+also) // 2
    if keresett < list[k]:
        felso = k-1
    elif keresett > list[k]:
        also=k+1
    else:
        kimenet = True, k
        break
else:
    kimenet = False

print(kimenet)