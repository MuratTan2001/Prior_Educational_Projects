import java.util.Scanner;

public class Q1 {
	public static void main(String[] args) {
	int first = 0;
	int second =0;
	Scanner myInput = new Scanner(System.in);
	for (int i = 0; i < 10; i++) {
			System.out.print("Enter Number:");
			int input = myInput.nextInt();
			System.out.println(input);
			
			if (first<input) {
				second= first;
				first= input;
			}
			else if (second <input) {
				second= input;
			}
			else{
			};

									};
	System.out.println("Largest number is: "+first);
	System.out.println("Second largest number is: "+second);
	}

}
