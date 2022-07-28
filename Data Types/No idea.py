# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = list(map(int,input().split()))

cf = list(map(int,input().split()))
d = list(map(int,input().split()))
e = list(map(int,input().split()))
result = 0
for i in cf:
    if i in d:
        result += 1
    elif i in e:
        result -= 1
print(result)