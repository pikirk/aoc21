data = []
with open("day3_input2.txt", "r") as input:
    data = input.read().splitlines()

def highest():
    cur_common = data
    for i in range (0, 12):
        if (len(cur_common) == 1):
            return cur_common

        ones = list(filter (lambda a: a[i : i+1] == '1',  cur_common))
        zeros = list(filter (lambda a: a[i : i+1] == '0',  cur_common))
        
        if len(ones) > len(zeros):
            cur_common = ones
        elif len(ones) == len(zeros):
            cur_common = ones
        elif len(zeros) > len(ones):
            cur_common = zeros
        else:
            print ('degenerate case')
    return cur_common

def lowest():
    cur_uncommon = data
    for i in range (0, 12):
        if (len(cur_uncommon) == 1):
            return cur_uncommon

        ones = list(filter (lambda a: a[i : i+1] == '1',  cur_uncommon))
        zeros = list(filter (lambda a: a[i : i+1] == '0',  cur_uncommon))

        if len(zeros) < len(ones):
            cur_uncommon = zeros
        elif len(ones) == len(zeros):
            cur_uncommon = zeros
        elif len(ones) < len(zeros):
            cur_uncommon = ones
        else:
            print ('degenerate case')
            
    return cur_uncommon

def toVal(mask):
    result = 0
    the_bit = ''
    for i in range (0, len(mask)):
        the_bit = mask[ i: (i + 1) ]
        if (the_bit == '1'):
            result += pow(2, ((len(mask) - 1) - i))
 
    return result

oxygen_bit = highest()
co2_bit = lowest()

# 3385170
print (toVal(oxygen_bit[0]) * toVal(co2_bit[0]))
