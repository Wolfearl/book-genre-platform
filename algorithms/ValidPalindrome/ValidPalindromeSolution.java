package ValidPalindrome;

/*
 * Условие: Проверить, является ли строка палиндромом
 * Подход: Two pointers с пропуском не-алфавитно-цифровых символов
 * Сложность: O(n) по времени, O(1) по памяти
 */

public class ValidPalindromeSolution {
    public static void main(String[] args) {
        // Test Case 1
        String s1 = "A man, a plan, a canal: Panama";
        System.out.println("Valid Palindrome: " + isPalindrome(s1));  // true
        
        // Test Case 2
        String s2 = "race a car";
        System.out.println("Valid Palindrome: " + isPalindrome(s2));  // false
    
        // Test Case 3
        String s3 = " ";
        System.out.println("Valid Palindrome: " + isPalindrome(s3));  // true
    }

    public static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(right)) != Character.toLowerCase(s.charAt(left))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    
}
