# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        if n == 1:
            return 0
        l, r = 0, n-1
        while l < r:
            m = l + r >> 1
            if (l - r & 1):
                tmp = reader.compareSub(l, m, m+1, r)
                if not tmp:
                    return m
                elif tmp == 1:
                    r = m
                else:
                    l = m + 1
            else:
                tmp = reader.compareSub(l, m, m, r)
                if not tmp:
                    return m
                elif tmp == 1:
                    r = m
                else:
                    l = m
                    
        return l