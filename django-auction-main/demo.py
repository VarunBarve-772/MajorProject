l = int(input())
arr = []
data = []

for a in range(l):
    arr.append(int(input()))

for x,i in enumerate(arr):
    if x == (len(arr) - 1):
        temp = abs(arr[x] - arr[0]) + abs((x+1) - 1)
    else:
        temp = abs(arr[x] - arr[x+1]) + abs((x+1) - (x+2))           
    data.append(temp)

print(max(data))