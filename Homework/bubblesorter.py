# Bubblesorter

list = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]

for k in range(0, len(list)):
    for i in range(1, len(list) - k):
        if list[i-1] > list[i]:
            list[i], list[i-1] = list[i-1], list[i]

print(list)