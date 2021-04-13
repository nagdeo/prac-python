import os

cars = [1,2,3,4,5,6,8,9,10]
for i in range(1,len(cars)+1):
        if(cars[i-1]!=i):
            print(i)
            break

cars2 = [1, 4, 3, 6, 5, 7, 8, 9, 10]

n=len(cars2)
tot=(n+1)*(n+2)/2
print(tot)
for i in range(1, len(cars2) + 1):
    tot-=cars2[i-1]
print(tot)
####################
cars1 = [1,7,3,2,5,9,8,10,6]
for i in range(1,len(cars1)+1):
    for j in range(1,len(cars1)+1):
        if(cars1[j-1]!=i):
            print(i)
            break