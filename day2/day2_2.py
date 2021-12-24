def increaseDepth(val, x, aim):
    result = 0
    if (len(x) == 0 or len(aim) == 0 ):
        result = 0
    else:
        result = aim [ len(aim) - 1 ] * val
    return result

def decreaseAim(val, aim):
    result = 0
    if (len(aim) == 0 ):
        result = 0
    else:
        result = aim[ len(aim) - 1 ] - val
    return result

data = []
with open("day2_input2.txt", "r") as input:
    data = input.read().splitlines()

cmd = []
x = []
y = []
aim = []
dir = ""
val = 0
result = 0

for i in range(0, len(data) ):
    cmd = data[i].split(" ")
    dir = cmd[0]
    val = int(cmd[1])
    if (dir == 'forward'):
        x.append(val)
        result = increaseDepth(val, x, aim) 
        y.append(result)

    elif (dir == 'down'):
        if (len(aim) == 0 ):
            aim.append(val)
        else:
            result = aim[len(aim) - 1] + val
            aim.append(result)

    elif (dir == 'up'):
        result = decreaseAim(val, aim )
        aim.append(result)

# 1568138742    
answer = sum(x[0 : len(x)]) * sum(y[0 : len(y)])
print (answer)

