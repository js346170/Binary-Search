import random
nums = [random.randint(0, 20) for i in range(10)]

def binarySearch(aList, num):
    #sort list
    aList.sort()
    # set up loop
    
    while aList:
        mid = len(aList)//2
        if aList[mid] == num:
            return True
        elif aList[mid] > num:
            aList = aList[:mid]
        elif aList[mid] < num:
            aList = aList[mid+1:]

        print(aList)
    
    # find middle index
    mid = len(aList)//2

    # print(mid)
    # check value of middle index
    if aList[mid] == num:
        return True

    # check if value is greater
    elif aList[mid] > num:
        aList = aList[:mid]
        # print(aList)

    # check if value is less
    elif aList[mid] < num:
        aList = aList[mid + 1:]
    # print(aList)
    return False
    



print(sorted(nums))
print(binarySearch(nums, 3))













