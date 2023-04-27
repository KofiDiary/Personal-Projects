def calcMean():
    sampleSpace = []
    counter = 0
    sum = 0
    
    print("\nPlease, once you have no more value to enter, enter -1 to break from loop.")
    
    while True:
        dataPoints = int(input("\nPlease enter your value: "))
        sampleSpace.append(dataPoints)
        counter += 1
        if dataPoints == -1:
            sampleSpace.pop(-1)
            counter -= 1
            break
        
    
    for regulator in range(0, counter):
        sum += sampleSpace[regulator]
        
    sum = sum / counter
    mean = sum
    print(f'\nMean = {mean}')
    
def calcMedian():
    sampleSpace = []
    counter = 0
    sum = 0
    
    print("\nPlease, once you have no more value to enter, enter -1 to break from loop.")
    
    while True:
        dataPoints = int(input("\nPlease enter your value: "))
        sampleSpace.append(dataPoints)
        counter += 1
        if dataPoints == -1:
            sampleSpace.pop(-1)
            counter -= 1
            break
        
    
    if counter % 2 == 0:
        sampleSpace.sort()
        counter = counter / 2
        frontCounter = counter - 1
        frontCounter = int(frontCounter)
        backCounter = -(counter)
        backCounter = int(backCounter)
        sum = (sampleSpace[frontCounter] + sampleSpace[backCounter]) / 2
        median = sum
        
        print(f'\nMedian = {median}')
    
    else:
        sampleSpace.sort()
        median = (counter + 1) / 2
        median -= 1
        median = int(median)
        print(f'\nMedian = {sampleSpace[median]}')
        
def calcStandard_Dev():
    sampleSpace = []
    counter = 0
    sum = 0
    Sum = 0
    
    print("\nPlease, once you have no more value to enter, enter -1 to break from loop.")
    
    while True:
        dataPoints = int(input("\nPlease enter your value: "))
        sampleSpace.append(dataPoints)
        counter += 1
        if dataPoints == -1:
            sampleSpace.pop(-1)
            counter -= 1
            break
        
    for regulator in range(0, counter):
        Sum += sampleSpace[regulator]
        
    Sum = Sum / counter
    mean = Sum
    
    for regulator in range(0, counter):
        sum += (sampleSpace[regulator] - mean)**2
        
    sum = sum / counter
    standardDeviation = sum
    print(f'\nStandard Deviation = {standardDeviation}')
    
def calcAll_Three():
    sampleSpace = []
    counter = 0
    sum = 0
    Sum = 0
    
    print("\nPlease, once you have no more value to enter, enter -1 to break from loop.")
    
    while True:
        dataPoints = int(input("\nPlease enter your value: "))
        sampleSpace.append(dataPoints)
        counter += 1
        if dataPoints == -1:
            sampleSpace.pop(-1)
            counter -= 1
            break
    
    for regulator in range(0, counter):
        Sum += sampleSpace[regulator]
        
    Sum = Sum / counter
    mean = Sum
    
    print(f'\nMean = {mean}')
    
    for regulator in range(0, counter):
        sum += (sampleSpace[regulator] - mean)**2
        
    sum = sum / counter
    standardDeviation = sum
    
    if counter % 2 == 0:
        sampleSpace.sort()
        counter = counter / 2
        frontCounter = counter - 1
        frontCounter = int(frontCounter)
        backCounter = -(counter)
        backCounter = int(backCounter)
        sum = (sampleSpace[frontCounter] + sampleSpace[backCounter]) / 2
        median = sum
        
        print(f'\nMedian = {median}')
    
    else:
        sampleSpace.sort()
        median = (counter + 1) / 2
        median -= 1
        median = int(median)
        print(f'\nMedian = {sampleSpace[median]}')
        
    
    print(f'\nStandard Deviation = {standardDeviation}')
    
def makeDecisions():
    print("Please select an option to perform operations. \n\n1. Calculate Mean \n\n2. Calculate Median \n\n3. Calculate Standard Deviation \n\n4. Calculate All Three")
    option = int(input("\n"))
    if option == 1:
        calcMean()
    elif option == 2:
        calcMedian()
    elif option == 3:
        calcStandard_Dev()
    elif option == 4:
        calcAll_Three()
    else:
        print("\nInvalid input!")
    
makeDecisions()