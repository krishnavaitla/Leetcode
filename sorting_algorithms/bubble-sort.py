def bubble(num):
    swapped = True
    while swapped:
        swapped = False
        print("swapped :", swapped)
        for i in range(len(num)-1):
            print("i :", num[i])
            print("i+1 :", num[i+1])
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
                swapped=True

lis=[5,32,6,7,3,2]
bubble(lis)
print(lis)

#steps:
#we want to compare 2 pairs from start to end till everything is sorted
#if first element greater than second once swap
#while loop runs until swapped is true
