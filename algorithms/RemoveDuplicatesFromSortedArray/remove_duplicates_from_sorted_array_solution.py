"""
Условие: Вернуть количество уникальных элементов массива
Подход: Two pointers (медленный и быстрый указатель)
Сложность: O(n) по времени, O(1) по памяти
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow = 0
    fast = 1
    count = 1
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            nums[count] = nums[fast]
            count += 1
        slow += 1
        fast += 1
    return count


# Тесты
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1,1,2]
    print(f"Number of unique elements: {removeDuplicates(nums1)}")  # 2
    
    # Test Case 2
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(f"Number of unique elements: {removeDuplicates(nums2)}")  # 5