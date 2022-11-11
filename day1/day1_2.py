# 0, 1, 2, 3, 4, 5, 6
# 0, 1, 2
#    1, 2, 3
#       2, 3, 4
#          3, 4, 5
#             4, 5, 6
#                5, 6
#                   6

data = []
with open("day1_input2.txt", "r") as input:
    tmp = input.read().splitlines()
    data = [ int(x) for x in tmp ]

depth_counter = 0
current = sum( data[0:2] )
test = 0

for w in range ( 2, len(data) - 1 ):
     lower = w - 2
     upper = w + 1
     test = sum (data [lower:upper] ) 
     if (test > current):
          depth_counter +=1
     current = test

# 1486
print('answer=' + str(depth_counter))

