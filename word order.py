
n = int(input())

words = {}
order = []

for i in range(n):
    word = input().strip()

    if word not in words:
        words[word] = 1
        order.append(word)
    else:
        words[word] += 1

print(len(words))
print(" ".join(str(words[word]) for word in order))
