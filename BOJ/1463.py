inp = int(input())

def make_to_one(n):
    memo = [0 for _ in range(n+1)]
    if n <= 3:
        if n == 1:
            memo[1] = 0
        elif n == 2:
            memo[2] = 1
        else:
            memo[3] = 1
    else:
        memo[1] = 0
        memo[2] = 1
        memo[3] = 1
        for i in range(4, n+1):
            temp = []
            temp.append(memo[i-1] + 1)
            if i % 3 == 0:
                temp.append(memo[i//3] + 1)
            if i % 2 == 0:
                temp.append(memo[i//2] + 1)
            memo[i] = min(temp)
    return memo[n]

print(make_to_one(inp))