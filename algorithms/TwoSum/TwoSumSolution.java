package TwoSum;

import java.util.Arrays;
import java.util.HashMap;

/*
 * Условие: Найти индексы двух чисел, которые в сумме дают target
 * Подход: Использование хэш-таблицы для хранения пройденных элементов
 * Сложность: O(n) по времени, O(n) по памяти
 */

 
public class TwoSumSolution {
    public static void main(String[] args) {
        // Test Case 1
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        System.out.println("Two Sum: " + Arrays.toString(twoSum(nums1, target1))); // [0, 1]
        
        // Test Case 2
        int[] nums2 = {3, 2, 4};
        int target2 = 6;
        System.out.println("Two Sum: " + Arrays.toString(twoSum(nums2, target2)));  // [1, 2]
    } 

    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> num_map = new HashMap<>(nums.length);
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if (num_map.containsKey(complement)) {
                return new int[] {num_map.get(complement), i};
            }
            num_map.put(nums[i], i);
        }
        return new int[0];
    }
 }