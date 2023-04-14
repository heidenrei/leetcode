class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        hasupper = any(x.isupper() for x in password)
        haslower = any(x.islower() for x in password)
        has8 = len(password) >= 8
        hasnum = any(x.isnumeric() for x in password)
        hasspec = any(x in "!@#$%^&*()-+" for x in password)
        hascon = any(password[i] == password[i-1] for i in range(1, len(password)))
        return hasupper and haslower and has8 and hasnum and hasspec and not hascon