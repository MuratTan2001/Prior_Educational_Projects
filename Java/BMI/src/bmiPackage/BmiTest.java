package bmiPackage;
import java.io.*;
import java.util.Scanner;
public class BmiTest {

	public static void main(String[] args) {
		Scanner myScanner = new Scanner(System.in);
		int Size=3;
		Bmi arrOfBMI[] = new Bmi[Size];
		for(int i=1;i<Size+1;i++) {
			System.out.println("---ENTER PERSON "+ i +"'S VALUES---");
			System.out.println("Enter name, age, weight, height: (as space separated)");
			String inputString = myScanner.nextLine();
			String[] arrOfStr = inputString.split(" ", 5);
			String name = arrOfStr[0] + " " + arrOfStr[1];
		 	int age = Integer.parseInt(arrOfStr[2]);
		 	double weight = Double.parseDouble(arrOfStr[3]);
		 	double height = Double.parseDouble(arrOfStr[4]);
		 	arrOfBMI[i-1] = new Bmi();
		 	arrOfBMI[i-1].setMeName(name);
		 	arrOfBMI[i-1].setMeAge(age);
		 	arrOfBMI[i-1].setMeWeight(weight);
		 	arrOfBMI[i-1].setMeHeight(height);
		}
		myScanner.close();
		for(int i=1;i<Size+1;i++) {
			System.out.println("** The BMI result for"+ arrOfBMI[i-1].getMeName()+ "( Age: "+ arrOfBMI[i-1].getMeAge()+" Weight: "+ arrOfBMI[i-1].getMeWeight()+ " Height: "+arrOfBMI[i-1].getMeHeight()+") is");
			System.out.println(arrOfBMI[i-1].getStatus(arrOfBMI[i-1].getBMI(arrOfBMI[i-1].getMeWeight(),arrOfBMI[i-1].getMeHeight())));
	}

}}
