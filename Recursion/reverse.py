def reverse(A):
    if len(A)==1:
        return A
    return reverse(A[1:]) + A[:1]

A = [1,2,3,4,5]
print(reverse(A))