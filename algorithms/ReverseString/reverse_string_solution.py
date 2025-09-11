"""
Условие: Развернуть строку на месте
Подход: Two pointers (начало и конец), обмен значениями
Сложность: O(n) по времени, O(1) по памяти
"""

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1
    return s


# Тесты
if __name__ == "__main__":
    # Test Case 1
    s1 = ["h","e","l","l","o"]
    print(f"Reverse String: {reverseString(s1)}")  # ["o","l","l","e","h"]
    
    # Test Case 2
    s2 = ["H","a","n","n","a","h"]
    print(f"Reverse String: {reverseString(s2)}")  # ["h","a","n","n","a","H"]