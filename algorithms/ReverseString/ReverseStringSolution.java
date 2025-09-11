package ReverseString;

/*
 * Условие: Развернуть строку на месте
 * Подход: Two pointers (начало и конец), обмен значениями
 * Сложность: O(n) по времени, O(1) по памяти
 */

public class ReverseStringSolution {
    public static void main(String[] args) {
        // Test Case 1
        char[] s1 = {'h','e','l','l','o'};
        reverseString(s1);
        System.out.println(s1); // ["o","l","l","e","h"]
        
        // Test Case 2
        char[] s2 = {'H','a','n','n','a','h'};
        reverseString(s2);
        System.out.println(s2); // ["h","a","n","n","a","H"]
    }

    public static void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        while (left < right) {
            char tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            left++;
            right--;
        }
    }
}
