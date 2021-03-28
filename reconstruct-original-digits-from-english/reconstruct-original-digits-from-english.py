class Solution:
    def originalDigits(self, s: str) -> str:
        N = len(s)
        ans = []
        d1 = ['zero', 'one', 'two', 'three',' four', 'five', 'six', 'seven', 'eight', 'nine']
        d2 = [Counter(x) for x in d1]
        c = Counter(s)
        
        if c['z'] > 0:
            ans.extend([0]*c['z'])
            c['e'] -= c['z']
            c['r'] -= c['z']
            c['o'] -= c['z']
            c['z'] = 0
        if c['w'] > 0:
            ans.extend([2]*c['w'])
            c['t'] -= c['w']
            c['o'] -= c['w']
            c['w'] = 0
        if c['u'] > 0:
            ans.extend([4]*c['u'])
            c['f'] -= c['u']
            c['o'] -= c['u']
            c['r'] -= c['u']
            c['u'] = 0
        if c['o'] > 0:
            ans.extend([1]*c['o'])
            c['n'] -= c['o']
            c['e'] -= c['o']
            c['o'] = 0
        if c['f'] > 0:
            ans.extend([5]*c['f'])
            c['i'] -= c['f']
            c['v'] -= c['f']
            c['e'] -= c['f']
            c['f'] = 0
        if c['x'] > 0:
            ans.extend([6]*c['x'])
            c['i'] -= c['x']
            c['s'] -= c['x']
            c['x'] = 0
        if c['v'] > 0:
            ans.extend([7]*c['v'])
            c['s'] -= c['v']
            c['e'] -= c['v']*2
            c['n'] -= c['v']
            c['v'] = 0
        if c['g'] > 0:
            ans.extend([8]*c['g'])
            c['e'] -= c['g']
            c['i'] -= c['g']
            c['h'] -= c['g']
            c['t'] -= c['g']
            c['g'] = 0
        if c['n'] > 0:
            ans.extend([9]*(c['n']//2))
            c['i'] -= c['n']//2
            c['e'] -= c['n']//2
            c['n'] = 0
        if c['t'] > 0:
            ans.extend([3]*c['t'])
        ans.sort()
        ans = [str(x) for x in ans]
        ans = ''.join(ans)
        return ans