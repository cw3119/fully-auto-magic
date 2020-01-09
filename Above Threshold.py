
def aboveThreshold(list1, threshold):
    count = 0
    for x in list1:
        if x > threshold:
            count+=1
    return(count)

list1 = [5, 9, 12, 100, 200, 3]
list2 = [8, 12, 14, 77, 700, 1000, 1001]
list3 = [1]
print(aboveThreshold(list1, 10))
print(aboveThreshold(list2, 10))
print(aboveThreshold(list3, 10))
