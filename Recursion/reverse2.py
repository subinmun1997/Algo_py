def reverse(A, start, stop):
    if start < stop:
        A[start], A[stop-1] = A[stop-1], A[start]
        reverse(A, start+1, stop-1)
    return A

A = [1,2,3,4,5]
start = 0
stop = 5
print(reverse(A, start, stop))