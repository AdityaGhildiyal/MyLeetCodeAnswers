class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if not digits:
            return []

        combinations = []
        for digit in digits:
            if not combinations:  
                combinations = [char for char in phone[digit]]
            else:
                temp = []
                for char in combinations:
                    for letter in phone[digit]:
                        temp.append(char + letter)
                combinations = temp

        return combinations

