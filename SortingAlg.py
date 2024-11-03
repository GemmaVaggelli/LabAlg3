import sys
from Nodi import Node

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    L = []
    R = []

    for i in range(0, q - p + 1):
        L.append(A[p + i])
    for j in range(0, r - q):
        R.append(A[q + j + 1])

    nodemax = Node('max')
    nodemax.f = -sys.maxsize
    L.append(nodemax)
    R.append(nodemax)

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i].f >= R[j].f:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
