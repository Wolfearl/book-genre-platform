"""
Условие: Найти индексы двух чисел, которые в сумме дают target
Подход: Использование хэш-таблицы для хранения пройденных элементов
Сложность: O(n) по времени, O(n) по памяти
"""

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Тесты
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Two Sum: {two_sum(nums1, target1)}")  # [0, 1]
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Two Sum: {two_sum(nums2, target2)}")  # [1, 2]