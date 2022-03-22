A = [1,23,5,322,12,42,2]

for __ in range(1 , len(A)):
    for j in range(len(A) - 1):
        if(A[j] > A[j + 1]):
            A[j],A[j + 1] = A[j + 1],A[j]
        else:
            continue
print(A)