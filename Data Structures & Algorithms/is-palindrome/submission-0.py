class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = s.lower()
        cleaned = "".join(char for char in lower_case if char.isalnum())
        return cleaned == cleaned[::-1]