import random
nums = [random.randint(0, 20) for i in range(10)]

def binarySearch(aList, num):
    aList.sort()
    while aList:
        mid = len(aList)//2
        if aList[mid] == num:
            return True
        elif aList[mid] > num:
            aList = aList[:mid]
        else:  # No need for elif, just use else
            aList = aList[mid+1:]
        print(aList)  # Optional debug
    return False  

print(sorted(nums))
print(binarySearch(nums, 3))