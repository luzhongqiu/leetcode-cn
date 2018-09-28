# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 说明：你不能倾斜容器，且 n 的值至少为 2。

# 示例:

# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49

# # 超出时间限制
# class Solution:
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         area = 0
#         l = len(height)
#         for i in range(l-1):
#             for j in range(i+1, l):
#                 _area = min(height[i], height[j]) * (j-i)
#                 area = max(area, _area)
#         return area

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        contain = 0
        while l < r:
            contain = max(contain, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return contain