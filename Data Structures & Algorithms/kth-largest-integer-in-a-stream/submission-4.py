class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numHeap = nums
        heapq.heapify(self.numHeap)
        self.k = k
        while len(self.numHeap) > k:
            heapq.heappop(self.numHeap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.numHeap, val)
        if len(self.numHeap) > self.k:
            heapq.heappop(self.numHeap)

        return self.numHeap[0]

        
