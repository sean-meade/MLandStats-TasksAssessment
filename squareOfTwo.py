num = 2
squareBase = 0

for i in range(1, num):
    if (i * i < num) and ((i + 1) * (i + 1) > num):
        squareBase = i
        
decimal = 1
decimalPlace = 0
squareOfTwo = str(squareBase)

for decPlace in range(1, 101):
    deciamlPlace = decimalPlace + 1
    decimal = decimal * 0.1
    multi = 10**decPlace
    decimal = round(decimal * multi)
    decimal = decimal/multi
    squareBase = round(squareBase * multi)
    squareBase = squareBase/multi
    for decNum in range(1, 10):
        decimalNumber = decimal * decNum
        decimalNumberPlus = decimal * (decNum + 1)
        testSquare = squareBase + decimalNumber
        testSquare = round(testSquare * multi)
        testSquare = testSquare/multi
        print(testSquare)
        testSquarePlus = squareBase + round(decimalNumberPlus, decPlace)
        if (((testSquare * testSquare) < num) and ((testSquarePlus * testSquarePlus) > num)):
            squareBase = squareBase + (decimal * (decNum))
            squareBase = round(squareBase * multi)
            squareBase = squareBase/multi
            repr(squareBase)
            break
            