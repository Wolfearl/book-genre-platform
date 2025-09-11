package RemoveDuplicatesFromSortedArray;

/*
 * Условие: Вернуть количество уникальных элементов массива
 * Подход: Two pointers (медленный и быстрый указатель)
 * Сложность: O(n) по времени, O(1) по памяти
 */

public class RemoveDuplicatesFromSortedArraySolution {
    public static void main(String[] args) {
        // Test Case 1
        int[] nums1 = {1,1,2};
        System.out.println("Number of unique elements:  " + removeDuplicates(nums1));  // 2
        
        // Test Case 2
        int[] nums2 = {0,0,1,1,1,2,2,3,3,4};
        System.out.println("Number of unique elements: " + removeDuplicates(nums2));  // 5
    }

    public static int removeDuplicates(int[] nums) {
        int slow = 0;
        int fast = 1;
        int count = 1;
        while (fast < nums.length) {
            if (nums[slow] != nums[fast]) {
                nums[count] = nums[fast];
                count++;
            }
            slow++;
            fast++;
        }
        return count;
    }
}
