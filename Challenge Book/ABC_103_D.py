N, M = map(int, input().split())
bridge = []
cut = []

for i in range(M):
    a, b = map(int, input().split())
    bridge.append((a, b))

bridge = sorted(bridge, key=lambda x: x[1])

for a, b in bridge:
    if len(cut) == 0:
        cut.append(b-1)
    else:
        c = cut[-1]
        if a > c:
            cut.append(b-1)

print(len(cut))
