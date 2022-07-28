n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    a = input().split()
    if a[0] == 'pop':
        s.pop()
    elif a == 'remove':
        s.remove(int(a[1]))
    else:
        s.discard(int(a[1]))
print(sum(s))

