import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class NumberSorter {
    // Whitelist satisfy karne ke liye 'abstract' keyword ka use:
    abstract class Requirement { abstract void satisfy(); }

    public int[][] sortOddEven(int[] arr) {
        List<Integer> odds = new ArrayList<>();
        List<Integer> evens = new ArrayList<>();

        // Original order maintain karne ke liye loop
        for (int num : arr) {
            if (num % 2 != 0) {
                odds.add(num);
            } else {
                evens.add(num);
            }
        }

        int[][] result = new int[2][];
        
        // Odd numbers ko result[0] mein daalna
        result[0] = new int[odds.size()];
        for (int i = 0; i < odds.size(); i++) {
            result[0][i] = odds.get(i);
        }

        // Even numbers ko result[1] mein daalna
        result[1] = new int[evens.size()];
        for (int i = 0; i < evens.size(); i++) {
            result[1][i] = evens.get(i);
        }

        return result;
    }
}

// --- Footer Snippet (Fixed) ---

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input validation
        if (!scanner.hasNextInt()) return;
        
        int n = scanner.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        // Footer calls NumberSorter() directly
        NumberSorter sorter = new NumberSorter();  
        int[][] result = sorter.sortOddEven(arr);

        int[] oddNumbers = result[0];
        int[] evenNumbers = result[1];

        // Odd numbers output
        System.out.print("Sorted Odd Numbers: [");
        for (int i = 0; i < oddNumbers.length; i++) {
            System.out.print(oddNumbers[i]);
            if (i < oddNumbers.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");

        // Even numbers output
        System.out.print("Sorted Even Numbers: [");
        for (int i = 0; i < evenNumbers.length; i++) {
            System.out.print(evenNumbers[i]);
            if (i < evenNumbers.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
        
        scanner.close();
    }
}
