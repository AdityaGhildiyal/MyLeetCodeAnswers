class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
      # Calculate area based on shorter wall and pointer distance
      area = min(height[left], height[right]) * (right - left)
      # Update max_area and move the pointer with the shorter height
      max_area = max(max_area, area)
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
    return max_area
