a = int(input().strip())
set_a = set(map(int, input().strip().split(' ')))
    
b = int(input().strip())
set_b = set(map(int, input().strip().split(' ')))
 
for i in sorted(set_a ^ set_b):
        print(i)