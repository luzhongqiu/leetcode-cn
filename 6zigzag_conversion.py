# 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

# 实现一个将字符串进行指定行数变换的函数:

# string convert(string s, int numRows);
# 示例 1:

# 输入: s = "PAYPALISHIRING", numRows = 3
# 输出: "PAHNAPLSIIGYIR"
# 示例 2:

# 输入: s = "PAYPALISHIRING", numRows = 4
# 输出: "PINALSIGYAHRPI"
# 解释:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        k = len(s)
        rstr = ""
        zlen = 2 * (numRows - 1)
        for i in range(0, numRows):
            n1 = 2 * (numRows-i-1)
            n2 = zlen - n1
 
            if n1 == 0 or n2 == 0:
                n1 = n2 = zlen
 
            j = 1
            index = i
            while index < k:
                rstr = rstr + s[index]
                if j % 2 != 0:
                    index = index + n1
                else:
                    index = index + n2
                j += 1
        return rstr

            
        