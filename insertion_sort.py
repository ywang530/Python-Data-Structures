def insertion_sort(A):
    for i in range(1, len(A)):
        print(A)
        cur = A[i]
        j = i
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

if __name__ == '__main__':
    A = [2, 4, 1, 3, 0]
    print(insertion_sort(A))