# Code related to Question 1
from statistics import median, mean

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Using sort() function to sort the list
ages.sort()

#Displaying Maximum and Minimus age
print("Minimum age is ",ages[0])
print("Maximum age is ",ages[-1])

ages.append(ages[0])
ages.append(ages[-2])
ages.sort()

#Calculating median
if(len(ages)%2==0):    #checking if the total number of elements in the list is odd

    median = (ages[int (len(ages)/2)-1] + ages[(int (len(ages)/2))])/2

    print("Median is ", median)

else:
    median = ages[int (len(ages)/2)]

    print("Median is ", median)

print("Average is ", mean(ages))

print("Range is ", ages[-1]-ages[0])

