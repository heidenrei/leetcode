class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        if sum(arr)%3 != 0:
            return [-1,-1]
        
        target_ones = sum(arr)//3
        
        idxs = []
        cnt = 0
        
        if 1 not in arr:
            return [0,len(arr)-1]
        
        tmp = [arr.index(1)]
        for i in range(len(arr)):

            if arr[i] == 1:
                if not tmp:
                    tmp.append(i)
                cnt += 1
            if cnt == target_ones:
                cnt = 0
                idxs.append(tmp + [i])
                tmp = []
        
        print(idxs)
        
        if arr[idxs[0][0]:idxs[0][1]+1] == arr[idxs[1][0]:idxs[1][1]+1] == arr[idxs[2][0]:idxs[2][1]+1]:
            zeros = arr[idxs[2][1]+1:].count(0)
            print(zeros)
            if idxs[1][0] - idxs[0][1] > zeros and idxs[2][0] - idxs[1][1] > zeros:
                print('!')
                return [idxs[0][1]+zeros, idxs[1][1]+1+zeros]
        
        return [-1,-1]