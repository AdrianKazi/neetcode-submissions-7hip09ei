class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = [str(d) for d in digits]
        number = int(''.join(digits))
        number += 1
        number = str(number)
        digits = [s for s in number]
        return digits