# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
coun = set()

for _ in range(n):
    c = input().strip()
    coun.add(c)

print(len(coun))
