import timeit
import random
from typing import List
from heapq import heappush, heappop

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        if not self.head or value < self.head.value:
            self.head = Node(value, self.head)
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            current.next = Node(value, current.next)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        return None

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        heappush(self.heap, value)

    def dequeue(self):
        return heappop(self.heap) if self.heap else None

def generate_tasks(n: int) -> List[str]:
    return ['enqueue' if random.random() < 0.7 else 'dequeue' for _ in range(n)]

def measure_time(queue, tasks):
    start_time = timeit.default_timer()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(random.randint(1, 100))
        else:
            queue.dequeue()
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    return total_time, total_time / len(tasks)

tasks = generate_tasks(1000)

list_queue = ListPriorityQueue()
heap_queue = HeapPriorityQueue()

list_total_time, list_avg_time = measure_time(list_queue, tasks)
heap_total_time, heap_avg_time = measure_time(heap_queue, tasks)

print(f'ListPriorityQueue: Total Time = {list_total_time}, Average Time = {list_avg_time}')
print(f'HeapPriorityQueue: Total Time = {heap_total_time}, Average Time = {heap_avg_time}')