number =int(input())
s1 = set(input().split());
number2 = int(input())
s2 = set(input().split());

s = s1.difference(s2)

print(len(s))