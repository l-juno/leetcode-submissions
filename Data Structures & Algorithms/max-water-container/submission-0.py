class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        end = len(heights) - 1
        largestArea = 0
        while front<end:
            width = end - front
            height = min(heights[front], heights[end])
            area = width * height
            largestArea = max(largestArea, area)
            if heights[front] >= heights[end]:
                end -= 1
            else:
                front += 1
        return largestArea


        