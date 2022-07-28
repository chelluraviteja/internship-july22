a = set(input().split())
c = int(input())
output = True

for i in range(c):
    b = set(input().split())
    if not b.issubset(a):
        output = False
    if len(b) >= len(a):
        output = False

print(output)