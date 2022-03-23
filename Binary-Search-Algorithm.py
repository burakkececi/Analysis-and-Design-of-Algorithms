A = [1,23,5,322,12,42,2]
A.sort()
searchedNumber = 322
i = 1 #left boundry
j = len(A) #rigth boundry
while(i<j):
    m = int((i+j)/2)
    if searchedNumber > A[m]:
        i = m + 1
    else:
        j = m
if searchedNumber == A[i]:
    location = i
else:
    location = 0
print(location)