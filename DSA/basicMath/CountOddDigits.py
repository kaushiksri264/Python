class CountOddDigits:
    def __init__(self,number):
        self.number = number
    
    def count_odd_digits(self):
        count = 0
        num = self.number
        while num > 0:
            if num%2==1:
                count += 1
            num = num//10
        return count

if __name__ == "__main__":
   
    N = 12345
    countDigits = CountOddDigits(N)
    print("Number of Odd digits: ",countDigits.count_odd_digits())

