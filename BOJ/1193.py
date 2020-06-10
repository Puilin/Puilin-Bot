#백준 1193

inp = int(input())

def forward_dir(x, y):
    count = 0
    x -= 1
    y += 1
    count += 1
    return (x, y, count)

def reverse_dir(x, y):
    count = 0
    x += 1
    y -= 1
    count += 1
    return (x, y, count)

def dir_changer(x, y):
    count = 0
    if x == 1:
        y += 1
        count += 1
        return (x, y, count)
    if y == 1:
        x += 1
        count += 1
        return (x, y, count)

def main(n):
    count = 1
    if n > 1:
        x, y = 1, 1
        dir_change = 0
        while count < n:
            if x == 1 and y == 1:
                x, y = 2, 1
                count += 1
                dir_change += 1
            elif (x == 1 or y == 1) and dir_change == 0:
                x, y, counter = dir_changer(x, y)
                count += counter
                dir_change = dir_change + 1
            elif dir_change == 1:
                while x > 1:
                    dir_change = 0
                    x, y, counter = forward_dir(x, y)
                    count += counter
                    if count == n:
                        break
                if y % 2 == 0:
                    continue
                while y > 1:
                    dir_change = 0
                    x, y, counter = reverse_dir(x, y)
                    count += counter
                    if count == n:
                        break
        print('%s/%s' %(y, x))
    else:
        print('1/1')
print(main(inp))