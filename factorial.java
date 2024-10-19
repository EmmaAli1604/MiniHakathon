/**
 * factorial
 */

import java.util.Scanner;

public class factorial {
    private static int factorial(int num){
        if (num == 1 || num == 0){
            return 1;
        }
        return num*factorial(num-1)*factorial(num-2);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingresa el numero no negativo para el factorial");
        int fact = scanner.nextInt();
        System.out.println(factorial(fact));
    }
}