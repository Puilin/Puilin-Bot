inp = input()
inp1 = inp.split('\n')
def padoban(n):
    memo = []
    for i in range(n+1):
        if i <= 3:
            memo.append(1)
        else:
            memo.append(memo[i-2] + memo[i-3])
    return memo[n]
for j in inp1:
    if j != inp1[0]:
        print(padoban(int(j)))
