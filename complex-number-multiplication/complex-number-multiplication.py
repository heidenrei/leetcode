class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_real, num1_img = num1.split('+')
        num1_real = int(num1_real)
        num1_img = int(num1_img[:-1])
        num2_real, num2_img = num2.split('+')
        num2_real = int(num2_real)
        num2_img = int(num2_img[:-1])
        
        first_term = num1_real * num2_real - num1_img * num2_img
        sec_term = num1_real * num2_img + num2_real * num1_img
        
        return str(first_term) + "+" + str(sec_term) + "i"