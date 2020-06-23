inp = input()
inp1 = inp.split(' ')
inp1 = inp1[1:]
def padoban(n):
    memo = []
    for i in range(n+1):
        if i <= 3:
            memo.append(1)
        else:
            memo.append(memo[i-2] + memo[i-3])
    return memo[n]
for j in inp1:
    print(padoban(int(j)))