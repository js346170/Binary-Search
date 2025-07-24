import pandas as pd

# Read CSV
df = pd.read_csv("names.csv")  # replace with your filename
# df = pd.read_excel("names.xlsx")
names = df["Name"].dropna().tolist()  # clean and extract the column

def binarySearchString(aList, target):
    aList.sort()
    while aList:
        mid = len(aList) // 2
        if aList[mid] == target:
            return True
        elif aList[mid] > target:
            aList = aList[:mid]
        else:
            aList = aList[mid + 1:]
    return False

# Example usage
print(sorted(names))
print(binarySearchString(names, "Charlie"))
