# 356 Line Reflection

from typing import (
    List,
)

class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def is_reflected(self, points: List[List[int]]) -> bool:
        """
        (x1, y) симмитрично (x2, y) относ center  x1 < x2
        <=>
        center - x1 == x2 - center
        x1 + x2 == 2 * center
        """
        if not points:
            return True
        min_x = points[0][0]
        max_x = points[0][0]
        points_set = set()
        for elem in points:
            x, y = tuple(elem)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            points_set.add((x, y))
        twice_center = min_x + max_x
        for x, y in points_set:
            if (twice_center - x, y) not in points_set:
                return False
        return True



s = Solution()
points = [[-1, 2], [0, -3], [1, 2], [2, 0], [3, 2], [4, -3], [5, 2]]


print(points)
print(s.is_reflected(points))