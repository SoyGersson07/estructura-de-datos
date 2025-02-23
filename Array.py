Array=[5,1,8,9,12]
for i in range(1, len(Array)):
    int= Array[i]
    j= i-1

    while j >=0 and Array[j] > int:
        Array[j + 1] = Array[j]
        j -= 1

    Array[j + 1] = int

print(Array)