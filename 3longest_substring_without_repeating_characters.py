# 给定一个字符串，找出不含有重复字符的最长子串的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 无重复字符的最长子串是 "abc"，其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 无重复字符的最长子串是 "b"，其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 无重复字符的最长子串是 "wke"，其长度为 3。
#      请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。


# 粗暴的方法， O(n2)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = 0
        last = 0
        max = 0
        for i in range(len(s)):
            same = {s[i]: i}
            first = i
            for j in range(i + 1,len(s)):
                if s[j] in same:
                    last = j - 1
                    break
                else:
                    same[s[j]] = j
                    last = j
            delta = last - first + 1
            max = max if max > delta else delta
        return max
            
# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_len = 0
        used = {}
        
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            used[s[i]] = i
            
        return max_len
