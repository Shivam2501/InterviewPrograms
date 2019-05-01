
# coding: utf-8

# In[33]:

n, k = raw_input().split()
n = int(n)
k = int(k)
array = raw_input().split()
for i in range(n):
    array[i] = int(array[i])


# In[36]:

def calculateSum(num):
    return (num*(num-1))//2

def calculateUpvotes(array):
    increasingRange = 0
    decreasingRange = 0
    
    currentLength = 1
    equalLength = 0
    lastIndex = True
    for i in range(1, len(array)):
        if lastIndex:
            if array[i] < array[i-1]:
                lastIndex = False
                if currentLength > 1:
                    increasingRange += calculateSum(currentLength)
                if equalLength > 0:
                    currentLength = equalLength + 1
                else:
                    currentLength = 2
                equalLength = 0
            elif array[i] == array[i-1]:
                if equalLength == 0:
                    equalLength = 2
                else:
                    equalLength += 1
                currentLength += 1
            else:
                currentLength += 1
        else:
            if array[i] > array[i-1]:
                lastIndex = True
                if currentLength > 1:
                    decreasingRange += calculateSum(currentLength)
                if equalLength > 0:
                    currentLength = equalLength + 1
                else:
                    currentLength = 2
                equalLength = 0
            elif array[i] == array[i-1]:
                if equalLength == 0:
                    equalLength = 2
                else:
                    equalLength += 1
                currentLength += 1
            else:
                currentLength += 1
                
    if currentLength > 1:
        if lastIndex:
            increasingRange += calculateSum(currentLength)
            if equalLength != 0:
                decreasingRange += calculateSum(equalLength)
        else:
            decreasingRange += calculateSum(currentLength)
            if equalLength != 0:
                increasingRange += calculateSum(equalLength)
    return increasingRange-decreasingRange


# In[37]:

# iterate through each window
for i in range(0, n-k+1):
    print(calculateUpvotes(array[i:i+k]))


# In[ ]:



