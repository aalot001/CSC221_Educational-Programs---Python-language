def smallest(aList):
    smallest = aList[0]
    for n, item in enumerate(aList):
        if smallest > aList[n]:
            smallest = aList[n]
    return smallest
def main():
    aList = [9,8,35,19,3,11,4]
    newHigh = smallest(aList)
    print(newHigh)
if __name__=="__main__":
    main()
