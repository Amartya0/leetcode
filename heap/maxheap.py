class maxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1)//2

    def leftChild(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def swap(self, findex, sindex):
        self.heap[findex], self.heap[sindex] = self.heap[sindex], self.heap[findex]

    def heapifyUp(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(self.parent(index), index)
            index = self.parent(index)

    def insert(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def heapifyDown(self, index):
        largest = index
        left = self.leftChild(index)
        right = self.rightChild(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(largest, index)
            self.heapifyDown(largest)

    def extractMax(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapifyDown(0)
            return root

    def getMax(self):
        return self.heap[0] if self.heap else None

    def buildHeap(self, arr):
        self.heap = arr
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapifyDown(i)
