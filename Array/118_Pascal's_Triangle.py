"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list_return = [[1]]
        for i in range(1, numRows):
            n = 1
            list_tem = []
            # list_tem.append(n)
            for j in range(0, i + 1):
                n = n * (i - j) / (j + 1)
                list_tem.append(n)
            list_return.append(list_tem)
        print (list_return)

x = Solution()
x.generate(5)