def quick_select(L, k):
    p = L[0]  # 6
    A, B, M = [], [], []  # p보다 작은 # p보다 큰 # p랑 같은

    for x in L:
        if p > x:
            A.append(x)
        elif p < x:
            B.append(x)
        else:
            M.append(x)

    if len(A) > k:
        return quick_select(A, k)
    elif len(A) + len(M) < k:
        return quick_select(B, k-len(A)-len(M))
    else:
        return p

L = [6, 5, 1, 7, 9, 3, 8, 10, 2]
print(quick_select(L,8))

