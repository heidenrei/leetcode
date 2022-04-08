class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        N = len(digits)
        # as long as there are > 1 unique non-zero digits we have an answer
        digits.sort()
        r = sum(digits)%3
        # either pull off 2 1s, 1 2 or 1 1
        # greedy from right side
        # if r == 2:
        # try pulling off 1st 2 from the right
        # else try pulling off 2 1s
        # if r == 1:
        # try pulling off the first 1
        if r == 1:
            flag = False
            for i in range(N):
                if digits[i] % 3 == 1:
                    digits = digits[:i] + digits[i+1:]
                    flag = True
                    break
            if flag:
                return str(int(''.join(str(x) for x in digits[::-1]))) if digits else ''
            
            # for a 1 we can also take out 2 2s
            flag = False
            for i in range(N):
                if digits[i] % 3 == 2:
                    digits = digits[:i] + digits[i+1:]
                    flag = True
                    break
            if flag == False:
                return ''
            for i in range(N):
                if digits[i] % 3 == 2:
                    digits = digits[:i] + digits[i+1:]
                    break
        elif r == 2:
            flag = False
            for i in range(N):
                if digits[i] % 3 == 2:
                    digits = digits[:i] + digits[i+1:]
                    flag = True
                    break
            if flag:
                return str(int(''.join(str(x) for x in digits[::-1]))) if digits else ''
            flag = False
            for i in range(N):
                if digits[i] % 3 == 1:
                    digits = digits[:i] + digits[i+1:]
                    flag = True
                    break
            if flag == False:
                return ''
            for i in range(N):
                if digits[i] % 3 == 1:
                    digits = digits[:i] + digits[i+1:]
                    break
        return str(int(''.join(str(x) for x in digits[::-1]))) if digits else ''
