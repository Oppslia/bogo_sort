import random
def makeRandomNumberList(low,high,amount):
    numList = []
    for spaces in range(0,amount):
        numList.append(random.randint(low,high))

    return numList

numberListOG:list = makeRandomNumberList(-50 ,100, 7)
numberList = numberListOG
# numberList:list = [-20, -19, -18, -17, -16, -15, -14, 13, -12]
inOrder = False
loopCount = 0


while inOrder == False:
    a = 0
    b = 1
    loopCount += 1
    print(numberList)
    while numberList[a] <= numberList[b]:
        if b == len(numberList)-1:
            inOrder = True
            print(F"Array Sorted\n{numberList}\n{loopCount}")
            break
        if numberList[a] <= numberList[b]:
            a += 1
            b += 1
            continue
    random.shuffle(numberList)
      

    