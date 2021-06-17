class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        vid = [math.inf for x in range(time+1)]
        vid[0] = 1
        clips.sort(key=lambda x: (x[0], -x[1]))
        
        clips = [[x, y] for x, y in clips if x <= len(vid)-1]
        
        for x, y in clips:
            if x != 0 and vid[x] != math.inf:
                for i in range(x, min(y+1, len(vid))):
                    if vid[i] == math.inf:
                        vid[i] = vid[x] + 1
                    else:
                        vid[i] = min(vid[i], vid[i-1]+1)
            else:
                for i in range(x, min(y+1, len(vid))):
                    if vid[x] != math.inf:
                        vid[i] = 1
                
        return vid[-1] if math.inf not in vid else -1
                    
        