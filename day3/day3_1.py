data = []
with open("day3_input.txt", "r") as input:
    data = input.read().splitlines()

first_bit_on = 0
second_bit_on = 0
third_bit_on = 0
fourth_bit_on = 0
fifth_bit_on = 0
sixth_bit_on = 0
seventh_bit_on = 0
eigth_bit_on = 0
ninth_bit_on = 0
tenth_bit_on = 0
eleventh_bit_on = 0
twelth_bit_on = 0

count = len(data)

def countBitOn( mask ):
    the_bit = ''
    global first_bit_on
    global second_bit_on 
    global third_bit_on 
    global fourth_bit_on 
    global fifth_bit_on
    global sixth_bit_on
    global seventh_bit_on
    global eigth_bit_on
    global ninth_bit_on
    global tenth_bit_on
    global eleventh_bit_on
    global twelth_bit_on

    for i in range (0, 12):
        the_bit = mask[ i: (i + 1) ]

        if (i == 0 and the_bit == '1'):
            twelth_bit_on +=1
        elif (i == 1 and the_bit == '1'):
            eleventh_bit_on +=1
        elif (i == 2 and the_bit == '1'):
            tenth_bit_on +=1
        elif (i == 3 and the_bit == '1'):
            ninth_bit_on +=1
        elif (i == 4 and the_bit == '1'):
            eigth_bit_on +=1
        elif (i == 5 and the_bit == '1'):
            seventh_bit_on +=1
        elif (i == 6 and the_bit == '1'):
            sixth_bit_on +=1
        elif (i == 7 and the_bit == '1'):
            fifth_bit_on +=1
        elif (i == 8 and the_bit == '1'):
            fourth_bit_on +=1    
        elif (i == 9 and the_bit == '1'):
            third_bit_on +=1
        elif (i == 10 and the_bit == '1'):
            second_bit_on +=1
        elif (i == 11 and the_bit == '1'):
            first_bit_on +=1

def calculateCommonBit():
    gamma_bit = ''
    mid = count / 2

    gamma_bit =  '1' if (twelth_bit_on > mid) else '0'
    gamma_bit +=  '1' if (eleventh_bit_on > mid) else '0'
    gamma_bit +=  '1' if (tenth_bit_on > mid) else '0'
    gamma_bit +=  '1' if (ninth_bit_on > mid) else '0'
    gamma_bit +=  '1' if (eigth_bit_on > mid) else '0'
    gamma_bit +=  '1' if (seventh_bit_on > mid) else '0'
    gamma_bit +=  '1' if (sixth_bit_on > mid) else '0'
    gamma_bit +=  '1' if (fifth_bit_on > mid) else '0'
    gamma_bit +=  '1' if (fourth_bit_on > mid) else '0'
    gamma_bit +=  '1' if (third_bit_on > mid) else '0'
    gamma_bit +=  '1' if (second_bit_on > mid) else '0'
    gamma_bit +=  '1' if (first_bit_on > mid) else '0'
    return gamma_bit

def calculateUnCommonBit( common_bit ):
    epsilon_bit = ''
    mid = count / 2

    epsilon_bit =  '0' if (twelth_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (eleventh_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (tenth_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (ninth_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (eigth_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (seventh_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (sixth_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (fifth_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (fourth_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (third_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (second_bit_on > mid) else '1'
    epsilon_bit +=  '0' if (first_bit_on > mid) else '1'
    return epsilon_bit   

def toVal(mask):
    result = 0
    the_bit = ''
    for i in range (0, 12):
        the_bit = mask[ i: (i + 1) ]

        if (i == 0 and the_bit == '1'):
            result += pow(2,11)
        elif (i == 1 and the_bit == '1'):
            result += pow(2,10)
        elif (i == 2 and the_bit == '1'):
            result += pow(2,9)
        elif (i == 3 and the_bit == '1'):
            result += pow(2,8)
        elif (i == 4 and the_bit == '1'):
            result += pow(2,7)
        elif (i == 5 and the_bit == '1'):
            result += pow(2,6)
        elif (i == 6 and the_bit == '1'):
            result += pow(2,5)
        elif (i == 7 and the_bit == '1'):
            result += pow(2,4)
        elif (i == 8 and the_bit == '1'):
            result += pow(2,3)
        elif (i == 9 and the_bit == '1'):
            result += pow(2,2)
        elif (i == 10 and the_bit == '1'):
            result += pow(2,1)
        elif (i == 11 and the_bit == '1'):
            result += pow(2,0)    
    return result

def answer():
    while (len(data) != 0 ):
        val = data.pop()
        countBitOn( val )

    result = calculateCommonBit()
    gamma = toVal(result)
    result = calculateUnCommonBit(result)
    epsilon = toVal(result)

    return gamma * epsilon

# 3882564
print( str(answer()) )
