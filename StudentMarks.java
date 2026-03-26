import java.util.Scanner;

public class StudentMarks {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of students: ");
        int n = sc.nextInt();

        // n students, 5 subjects
        int[][] marks = new int[n][5];

        // Input marks
        for (int i = 0; i < n; i++) {
            System.out.println("Enter marks of 5 subjects for student " + (i + 1));
            for (int j = 0; j < 5; j++) {
                marks[i][j] = sc.nextInt();
            }
        }

        // Display records using enhanced for loop
        System.out.println("\nStudent Records:");
        int studentNo = 1;
        for (int[] student : marks) {
            System.out.print("Student " + studentNo + ": ");
            for (int m : student) {
                System.out.print(m + " ");
            }
            System.out.println();
            studentNo++;
        }

        sc.close();
    }
}