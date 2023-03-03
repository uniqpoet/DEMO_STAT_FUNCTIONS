"""

Write a Python script to calculate the sum of numbers in a list, the
mean (or average) value of that list, and the standard deviation for
the list.

You should create three functions:  totalFun, meanFun, and devFun

To calculate standard deviation you have to:
    
    1. Calculate the mean
    2. Sum the difference of each number and the mean and square it
    3. Divide that sum by length of your list of numbers minus 1
    4. Take the square root that
    
                __________________
deviation =    / sum[(x - mean)^2]
              /-------------------
            \/        (n - 1)



    TO BE DONE:
    1. Mean Function, meanFun

    This is kinda fun
    
"""

# Define a function totalFun
# Input: a list
# Output: a single value representing the sum
def totalFun(aList):
    sum = 0
    for i in range(len(aList)):
        sum += aList[i]
    return sum

# Define a function meanFun
# Input: a list
# Output: a single value representing the mean (average)
# HINT:  the total sum can be calculated using the totalFun
# function above


def meanFun(somelist):    
    sum = 0        
    for x in somelist:
        sum = sum + x
    listitems = len(somelist)
    return sum/listitems


# Define a function devFun
# Input: a List
# Output: a single value representing the standard deviation
def devFun(aList):
    mean = meanFun(aList)
    sum = 0
    for i in range(len(aList)):
        diff = aList[i] - mean
        sq_diff = diff ** 2
        sum += sq_diff
    inner = sum / (len(aList) - 1)
    
    # Get sqrt() function from math
    from math import sqrt
    
    # Return the result
    return sqrt(inner)
    
        

# Main Program
theList = [1,2,3,4,5]

print("The sum of the list is %0.2f" % totalFun(theList))
print()
print("The mean of the list is %0.2f" % meanFun(theList))
print()
print("The standard deviation of the list is %0.2f" % devFun(theList))
print()









