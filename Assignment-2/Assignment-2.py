myNums = []

def readData():
    myNums
    myNums = []
    while True:
        try:
            num = float(input("Enter a number: "))
            myNums.append(num)
        except:
            break
    return myNums

readData()
# enter a list from user and store the input in myNums


def mean_Calc(myNums):
    mySum=sum(myNums)
    count = len(myNums)
    return mySum/count

def median_Calc(myNums):
    myNums.sort()
    count = len(myNums)
    if count % 2 == 0:
        mid = count // 2
        return (myNums[mid-1] + myNums[mid]) / 2
    else:
        mid = count // 2
        return myNums[mid]
    
def mode_Calc(myNums):
    myNums.sort()
    count = len(myNums)
    maximumCount = 0
    mode = myNums[0] #myNums=[1,3,2,4,3,4,3,4,1], count=9
    i = 0
    while i < count:
        thisNum = myNums[i]
        thisCount = myNums.count(thisNum)
        if thisCount > maximumCount:
            maximumCount = thisCount
            mode = thisNum
        i += thisCount
    return mode

# calculating Variance (step 2)
def calculate_variance(numbers):
    total_sum = 0  # Initialize sum to calculate mean
    count = 0  # Initialize count to get number of elements

    # Calculate total sum and count elements
    for num in numbers:
        total_sum += num
        count += 1

    mean = total_sum / count  # Compute mean manually

    squared_diffs_sum = 0  # Initialize sum for squared differences

    # Compute squared differences from mean
    for num in numbers:
        difference = num - mean  # Calculate difference from mean
        squared_difference = difference * difference  # Square it
        squared_diffs_sum += squared_difference  # Add to sum

    variance = squared_diffs_sum / count  # Compute final variance

    return variance  # Return result

# calculating Standard Deviation (step 3)
def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)  # Calculate variance
    standard_deviation = variance ** 0.5  # Compute square root of variance

    return standard_deviation  # Return result

# calculating euclidean distances (step 4)
def euclidean_distance(a, b):

    # Case 1: If both inputs are single numbers (int or float)
    if type(a) in [int, float] and type(b) in [int, float]:

        # Absolute difference
        if a > b:
            return a - b
        else:
            return b - a  
        

    # Case 2: If both inputs are lists of equal length
    if type(a) == list and type(b) == list:
        length_a = 0  # Counter for elements in list a
        length_b = 0  # Counter for elements in list b

        for _ in a:  
            length_a += 1
        for _ in b:  
            length_b += 1

        if length_a != length_b:  
            raise ValueError("Both lists must have the same number of elements.")

        sum_of_squares = 0  # Initialize sum of squared differences
        index = 0  

        # Calculate squared differences manually
        while index < length_a:
            difference = a[index] - b[index]  # Compute difference
            squared_difference = difference * difference  # Square it
            sum_of_squares += squared_difference  # Accumulate sum
            index += 1  # Move to next index

        return sum_of_squares ** 0.5  # Return square root of sum

    # Case 3: If neither of the above conditions are met
    raise ValueError("Both inputs should be numbers or lists of equal length.")

# calculating sigmoid function (step 5)
def sigmoid(x):
    return 1 / (1 + (2.71828 ** -x))