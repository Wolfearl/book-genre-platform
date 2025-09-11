package BestTimeToBuyAndSellStock;

/*
 * Условие: Найти максимальную прибыль от покупки и продажи акций
 * Подход: One pass с отслеживанием минимальной цены
 * Сложность: O(n) по времени, O(1) по памяти
 */

public class BestTimeToBuyAndSellStockSolution {
    public static void main(String[] args) {
        // Test Case 1
        int[] prices1 = {7,1,5,3,6,4};
        System.out.println("Max Profit: " + maxProfit(prices1));  // 5
        
        // Test Case 2
        int[] prices2 = {7,6,4,3,1};
        System.out.println("Max Profit: " + maxProfit(prices2));  // 0
    }

    public static int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int currentMaxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            else if (prices[i] - minPrice > currentMaxProfit) {
                currentMaxProfit = prices[i] - minPrice;
            }
        }
        return currentMaxProfit;
    }
    
}
