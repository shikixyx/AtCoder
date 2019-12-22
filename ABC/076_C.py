S = input()
T = input()

len_s = len(S)
len_t = len(T)

match = -1

for i in range((len_s - len_t), -1, -1):
    for j in range(len_t):
        if T[j] != S[i+j] and S[i+j] != "?":
            break

        if j == len_t-1:
            match = i

    if match != -1:
        break

if match == -1:
    print("UNRESTORABLE")
    exit()

list_s = list(S)

for i in range(match, match+len_t):
    list_s[i] = T[i - match]

list_s = [x if x != "?" else "a" for x in list_s]

print("".join(list_s))
