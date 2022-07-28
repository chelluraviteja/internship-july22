a = int(input())

b = map(int, input().split())
c = sorted(b)

for i in range(len(c)):
    if(i != len(c)-1):
        if(c[i]!=c[i-1] and c[i]!=c[i+1]):
            print(c[i])
            break;
    else:
        print(c[i])