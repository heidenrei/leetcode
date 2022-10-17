class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphas = set([x for x in 'qwertyuiopasdfghjklzxcvbnm'])
        
        if set(sentence) == alphas:
            return True
        else:
            return False