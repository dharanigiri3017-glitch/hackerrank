from collections import Counter

n = int(input())
sizes = list(map(int, input().split()))

shoes = Counter(sizes)

customers = int(input())
total = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        total += price
        shoes[size] -= 1

print(total)
