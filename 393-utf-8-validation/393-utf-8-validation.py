class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        N = len(data)
        data = [bin(x)[2:].zfill(8) for x in data]
        
        idx = 0
        
        while idx < len(data):
            if data[idx][0] == '0':
                idx += 1
            elif data[idx][0] == '1':
                tmp_idx = 0
                while tmp_idx <= 3 and data[idx][tmp_idx] == '1':
                    tmp_idx += 1
                if data[idx][tmp_idx] != '0' or tmp_idx == 1:
                    return False
                
                for _ in range(tmp_idx-1):
                    idx += 1
                    if idx >= N:
                        return False
                    if data[idx][:2] != '10':
                        return False
                idx += 1
                
        return True