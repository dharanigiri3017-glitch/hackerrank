thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * (2 * i + 1)).center(thickness * 2 - 1))

# Top Pillars
for i in range(thickness + 1):
    print(' ' * (thickness // 2) +
          c * thickness +
          ' ' * (thickness * 3) +
          c * thickness)

# Middle Belt
for i in range((thickness + 1) // 2):
    print(' ' * (thickness // 2) +
          c * (thickness * 5))

# Bottom Pillars
for i in range(thickness + 1):
    print(' ' * (thickness // 2) +
          c * thickness +
          ' ' * (thickness * 3) +
          c * thickness)

# Bottom Cone
for i in range(thickness):
    print(' ' * (thickness * 4 + i) +
          c * (thickness * 2 - 1 - 2 * i))
