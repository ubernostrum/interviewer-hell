/**
 * Utility class for detecting numbers that are perfect squares.
 * 
 * @author ubernostrum
 * @version 1.414
 * @since 1.414
 */
public class SquareDetector {
    // No instantiation for you.
    private SquareDetector() {}

    /**
     * Determines whether the given number is a perfect square.
     * @param n the number to check.
     */
    public static boolean isSquare(int n) {
        // Negative numbers aren't squares.
        if (n < 0) {
            return false;
        }

        // Zero is a square.
        if (n == 0) {
            return true;
        }

        long total = 0;
        int next = 1;

        while (total <= n) {
            total += next;
            if (total == n) {
                return true;
            }
            next += 2;
        }
        return false;
    }

    /**
     * When run with a numeric value as the first and only command-line argument,
     * outputs whether that value is a perfect square.
     */
    public static void main(String[] args) {
        int input;

        try {
            input = Integer.parseInt(args[0]);
        } catch (ArrayIndexOutOfBoundsException | NumberFormatException e) {
            System.out.println("Please provide a numeric argument.");
            return;
        }

        if (isSquare(input)) {
            System.out.printf("%d is a square.\n", input);
        } else {
            System.out.printf("%d is not a square.\n", input);
        }
    }
}
