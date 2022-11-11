data = []
with open('day1_input.txt') as input:
     data = input.readlines()

depth_counter = 0
test = 0
current = int( data[0].rstrip("\n") )

for r in range(1, ( len(data)) ):
    test = int( data[r].rstrip("\n") )
    if ( test > current ):
        depth_counter +=1
    current = test

# answer = 1446
print(depth_counter)
