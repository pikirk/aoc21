data = []
with open("day2_input.txt", "r") as input:
    data = input.read().splitlines()

cmd = []
x = []
y = []
dir = ""
val = 0

for i in range(0, len(data) ):
    cmd = data[i].split(" ")
    dir = cmd[0]
    val = int(cmd[1])
    if (dir == 'forward'):
        x.append(val)
    elif (dir == 'down'):
        y.append(val)
    elif (dir == 'up'):
        y.append(val * -1)

# 1427868    
answer = sum(x[0 : len(x)]) * sum(y[0 : len(y)])
print (answer)

