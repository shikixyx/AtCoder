import sys
import heapq
import copy

# プライオリティーキュー
# heapq


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt


N = int(input())
A = list(map(int, sys.stdin.readline().split()))

sum_h1 = [0] * (N+1)
sum_h2 = [0] * (N+1)

'''
N=2
0 1 2 3 4 5 6
3 1 4 1 5 9
'''

h1 = A[0:N]
h2 = A[N*2:N*3]

heapq.heapify(h1)
heapq._heapify_max(h2)

#print("h1", h1)
#print("h2", h2)
sum_h1[0] = sum(h1)
sum_h2[N] = sum(h2)

for k in range(N):
    #print("A[N+k]", A[N+k])
    #print("k+1", k+1)

    sum_h1[k+1] = sum_h1[k]
    sum_h1[k+1] += A[N+k]
    a = heapq.heappushpop(h1, A[N+k])
    sum_h1[k+1] -= a

    #sum_h1[k+1] = sum(h1)

    #print("A[2*N-k-1]", A[2*N-k-1])
    #print("N-k-1", N-k-1)

    sum_h2[N-k-1] = sum_h2[N-k]
    sum_h2[N-k-1] += A[2*N-k-1]
    _heappush_max(h2, A[2*N-k-1])
    sum_h2[N-k-1] -= _heappop_max(h2)

    #sum_h2[N-k-1] = sum(h2)


mx = None

#print("sum_h1", sum_h1)
#print("sum_h2", sum_h2)

for i in range(N+1):
    a = sum_h1[i] - sum_h2[i]

    if(mx == None or a > mx):
        mx = a

print(mx)

'''
for i in range(N+1):
    h1 = A[0:N+i]
    h2 = A[N+i:N*3]

    heapq.heapify(h1)
    heapq._heapify_max(h2)

    for k in range(N):
        if i <= k:
            _heappop_max(h2)
        else:
            heapq.heappop(h1)

    s = sum(h1) - sum(h2)

    if (mx == None or s > mx):
        mx = s
'''
