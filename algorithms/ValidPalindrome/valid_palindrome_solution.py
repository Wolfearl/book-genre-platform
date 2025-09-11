"""
Условие: Проверить, является ли строка палиндромом
Подход: Two pointers с пропуском не-алфавитно-цифровых символов
Сложность: O(n) по времени, O(1) по памяти
"""

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[right].lower() != s[left].lower():
            return False
        right -= 1
        left += 1
    return True


# Тесты
if __name__ == "__main__":
    # Test Case 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Valid Palindrome: {isPalindrome(s1)}")  # true
    
    # Test Case 2
    s2 = "race a car"
    print(f"Valid Palindrome: {isPalindrome(s2)}")  # false

    # Test Case 3
    s3 = " "
    print(f"Valid Palindrome: {isPalindrome(s3)}")  # true