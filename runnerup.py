a = int(input())
arr = list(map(int , input().split()))
k = max(arr);
while max(arr)==k:
    arr.remove(max(arr))
z=max(arr);
print(z)


