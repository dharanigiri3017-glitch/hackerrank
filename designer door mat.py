
n, m = map(int, input().split())

# Upper half
for i in range(n // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, "-"))

# Center
print("WELCOME".center(m, "-"))

# Lower half
for i in range(n // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, "-"))

