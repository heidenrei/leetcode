class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        c = Counter([x for x in senate])
        bansr = 0
        bansd = 0
        remd = c['D']
        remr = c['R']
        if not remd:
            return "Radiant"
        elif not remr:
            return "Dire"
        removed = set()
        while 1:
            for i, x in enumerate(senate):
                if i in removed:
                    continue
                if x == 'D':
                    if bansd:
                        bansd -= 1
                        removed.add(i)
                    else:
                        bansr += 1
                        remr -= 1
                        if not remr:
                            return 'Dire'
                else:
                    if bansr:
                        bansr -= 1
                        removed.add(i)
                    else:
                        bansd += 1
                        remd -= 1
                        if not remd:
                            return 'Radiant'