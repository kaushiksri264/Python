import math
class CountDigits:
    def __init__(self,digit):
        self.digit = digit

    #Brute-Force Approach - Time Complexity - O(log n), Space Complexity - O(1)    
    def count_digit(self):
        count = 0
        num = self.digit
        if num == 0:
            return 1
        while num > 0:
            count += 1
            num //=10
        return count
    #Optimal Approach - Time Complexity - O(1), Space Complexity - O(1)
    def digits_count(self):
        num = self.digit
        count = int(math.log10(num) + 1)
        return count

if __name__ == "__main__":
    n = 1000
    cnt = CountDigits(n)
    print("Count :",cnt.digits_count())
 