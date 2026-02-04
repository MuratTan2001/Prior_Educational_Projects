import java.util.Scanner;
import java.util.*;
public class Q2 {

	public static void main(String[] args) {
	    Scanner myScanner = new Scanner(System.in);
		while(true){
			System.out.print("Enter initial star number:");
			String inputString = myScanner.nextLine();
				if(inputString.equals("q")) {
					System.out.println("Program Terminates");
					break;}
			System.out.println(inputString);
			int inputNum = Integer.parseInt(inputString);
			int c =inputNum;
			int a=0;
			while(c>1) {
				for(int count =a; count>0;count= count-1) {
					System.out.print( " " );
				};
				// a amount of spaces
				for(int count =c; count>0;count= count-1) {
					System.out.print( "*" );
				};
				// c amount of stars
				a = a + 1;
				c = c - 2;
				if (c>0) {System.out.println( );};
			};
//	System.out.println( );
			while(c<=inputNum) {
				for(int count =a; count>0;count= count-1) {
					System.out.print( " " );
				};
				for(int count =c; count>0;count= count-1) {
					System.out.print( "*" );
				};
				a = a - 1;
				c = c + 2;
				System.out.println( );
			};
		};

	}

}
