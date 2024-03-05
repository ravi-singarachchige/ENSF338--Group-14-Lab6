import heapq

class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        heapq.heapify(self.heap)

    def enqueue(self, item):
        heapq.heappush(self.heap, item)

    def dequeue(self):
        return heapq.heappop(self.heap)
    

def test_heap_property(heap):
    n = len(heap)
    for i in range(n):
        if 2*i + 1 < n:
            assert heap[i] <= heap[2*i + 1]
        if 2*i + 2 < n:
            assert heap[i] <= heap[2*i + 2]

def test_heap():
    # Test case 1: Input array is already a correctly sorted heap
    heap = Heap()
    heap.heapify([1, 2, 3, 4, 5])
    test_heap_property(heap.heap)

    # Test case 2: Input array is empty
    heap = Heap()
    heap.heapify([])
    test_heap_property(heap.heap)

    # Test case 3: Input array is a long, randomly shuffled list of integers
    heap = Heap()
    heap.heapify([9, 3, 5, 7, 1, 2, 6, 8, 4])
    test_heap_property(heap.heap)

test_heap()