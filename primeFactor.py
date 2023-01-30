import math

def primeNum():
    number = True
    while number < 2:
        print('Put a number ')
        number = int(float(input()))
    # print(number, type(number))

    # print(math.sqrt(number))
    countBoard = []
    for n in range(2, math.ceil(math.sqrt(number)) + 1):
        countBoard.append(n)
    # print(number, len(countBoard), countBoard)

    dividerBoard = []
    for n in range(0, len(countBoard)):
        # print(countBoard[n])
        if number % countBoard[n] == 0:
            dividerBoard.append(countBoard[n])
        else:
            print(f'{number} divided for {countBoard[n]} is wrong')
    # print(dividerBoard)

    if len(dividerBoard) == 0:
        print(f'Number {number} is a prime number.')
    else:
        print(f'Number {number} is not a prime number.')

primeNum()
