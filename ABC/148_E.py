N = int(input())

if N % 2 == 1:
    print(0)
    exit()

num = 0
five = 0
N_5 = N // 2

while(True):
    if N_5 >= 5:
        N_5 = N_5 // 5
        five += 1
    else:
        break

N = N // 2

for i in range(1, five+1):
    f = 5 ** i
    num += N // f

print(num)
