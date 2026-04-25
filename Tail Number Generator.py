import random

LONG_LENGTH_BIAS = .1 # default .1
# this constant only affects the final character of length two tail numbers
CHANCE_OF_NUMBER_LENGTH_TWO = .2941 # default .2941
# these two constants affect the final character(s) of length 3-5 tail numbers
TWO_LETTERS_CHANCE = .3714 # default .3714
LETTER_OR_NUMBER = .2621 # default .2621

def validateLetter(asciiNumber): # regenerate letter if "I" or "O" is chosen
    if asciiNumber < 65 or asciiNumber > 90:
        return print("Invalid ascii index passed to validation")
    while asciiNumber == 73 or asciiNumber == 79:
        asciiNumber = random.randint(65, 90)
    return str(chr(asciiNumber))
    
# Determine length of each individual tail number 
def determineLengthOfNextTailNumber(minLen, maxLen):
    differenceInLengths = maxLen - minLen
    randomNum = random.random()
    match differenceInLengths:
        case 0: # minLen = maxLen
            return maxLen
        case 1:
            if randomNum > LONG_LENGTH_BIAS:
                return maxLen
            else:  
                return minLen
        case 2: 
            if randomNum > LONG_LENGTH_BIAS:
                return maxLen
            elif randomNum > LONG_LENGTH_BIAS**2:
                return maxLen - 1
            else:
                return minLen
        case 3: 
            if randomNum > LONG_LENGTH_BIAS:
                return maxLen
            elif randomNum > LONG_LENGTH_BIAS**2:
                return maxLen - 1
            elif randomNum > LONG_LENGTH_BIAS**3:
                return maxLen - 2
            else:
                return minLen
        case 4:
            if randomNum > LONG_LENGTH_BIAS:
                return maxLen
            elif randomNum > LONG_LENGTH_BIAS**2:
                return maxLen - 1
            elif randomNum > LONG_LENGTH_BIAS**3:
                return maxLen - 2
            elif randomNum > LONG_LENGTH_BIAS**4:
                return maxLen - 3
            else:
                return minLen
        case _:
            return print("Invalid difference passed to function")

# Return letter or number for last character as needed
def returnLetterOrNumber(chosenPercent):
    if random.random() < chosenPercent:
        return str(random.randint(0,9))
    else:
        return validateLetter(random.randint(65,90))

# Generate each individual tail number
def generateEachTailNumber(length):
    match length:
        case 1:
            return str("N" + str(random.randint(1,9)))
        case 2:
            return str("N" + str(random.randint(1,9)) + returnLetterOrNumber(CHANCE_OF_NUMBER_LENGTH_TWO)) 
        case 3:
            randNumber = random.random()
            if randNumber < TWO_LETTERS_CHANCE:
                return str("N" + str(random.randint(10,99)) + returnLetterOrNumber(LETTER_OR_NUMBER)) 
            else:
                return str("N" + str(random.randint(1,9)) + validateLetter(random.randint(65,90)) + validateLetter(random.randint(65,90)))
        case 4:
            randNumber = random.random()
            if randNumber < TWO_LETTERS_CHANCE:
                return str("N" + str(random.randint(100,999)) + returnLetterOrNumber(LETTER_OR_NUMBER)) 
            else:
                return str("N" + str(random.randint(10,99)) + validateLetter(random.randint(65,90)) + validateLetter(random.randint(65,90)))
        case 5:
            randNumber = random.random()
            if randNumber < TWO_LETTERS_CHANCE:
                return str("N" + str(random.randint(1000,9999)) + returnLetterOrNumber(LETTER_OR_NUMBER)) 
            else:
                return str("N" + str(random.randint(100,999)) + validateLetter(random.randint(65,90)) + validateLetter(random.randint(65,90)))
        case _:
            return print("Invalid length passed to function")
                
            
# Generate list of tail numbers, output to terminal
# TODO add file output option
def generateTailNumberList(minLen, maxLen, listLength):
    while minLen < 1 or minLen > 5 or maxLen < 1 or maxLen > 5:
        print("Invalid tail number length specified (must be 1-5 inclusive)\n")
        minimumTailNumberLength = int(input("What should the minimum tail number length be?\n"))
        maximumTailNumberLength = int(input("What should the maximum tail number length be?\n"))
    while listLength < 1:
        print("Invalid list length given. Try again. (Must be > 0)\n")
        numTailNumbersGenerated = int(input("How many tail numbers should be generated?\n"))
    if minLen > maxLen:
        minLen, maxLen = maxLen, minLen
        print("Minimum and maximum switched\n")
    for x in range(0, listLength):
        currentTailNumber = generateEachTailNumber(determineLengthOfNextTailNumber(minLen, maxLen))
        print(str(x + 1) + ": " + str(currentTailNumber))
        
while True:
    minimumTailNumberLength = int(input("What should the minimum tail number length be?\n"))
    maximumTailNumberLength = int(input("What should the maximum tail number length be?\n"))
    numTailNumbersGenerated = int(input("How many tail numbers should be generated?\n")) 
    generateTailNumberList(minimumTailNumberLength, maximumTailNumberLength, numTailNumbersGenerated)
    userWantsToContinue = str(input("\nGenerate more tail numbers? (y/n)\n"))
    if userWantsToContinue != "y":
        break
    else:
        print("")
