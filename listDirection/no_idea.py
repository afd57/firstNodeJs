line = input()
line = line.split()
n = int(line[0])
m = int(line[1])

main_set = input().split()
set_a = input().split()
set_b = input().split()

happy_score = 0

for i in range(n):
    if main_set[i] in set_a:
        happy_score += 1
    elif main_set[i] in set_b:
        happy_score -= 1
print(happy_score)