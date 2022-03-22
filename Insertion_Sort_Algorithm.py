A = [1,23,5,322,12,42,2]

for step in range(1, len(A)):
    key = A[step]
    j = step - 1
    while j >= 0 and key < A[j]:
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key
print(A)
    