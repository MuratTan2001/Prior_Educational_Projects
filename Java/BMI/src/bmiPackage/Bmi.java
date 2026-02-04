package bmiPackage;
import java.io.*;
public class Bmi {
	private String name;
	private int age;
	private double weight;
	private double height;
	public static final double KILOGRAMS_PER_POUND =0.45359237;
	public static final double METERS_PER_INCH = 0.0254;
	Bmi(){
		name ="John Black";
		age =25;
		weight =100;
		height =50;
	}
	Bmi(String name_t, double weight_t,double height_t){
		name= name_t;
		age = 20;
		weight = weight_t;
		height = height_t;
	}
	
	Bmi(String name_t,int age_t, double weight_t,double height_t){
		name= name_t;
		age = age_t;
		weight = weight_t;
		height = height_t;
	}
	public String getMeName() {return name;}
	public int getMeAge() {return age;}
	public double getMeWeight() {return weight;}
	public double getMeHeight() {return height;}
	
	public void setMeName(String name_set) {name=name_set;}
	public void setMeAge(int age_set) {age = age_set;}
	public void setMeWeight(double weight_set) {weight=weight_set;}
	public void setMeHeight(double height_set) {height=height_set;}
	
	public static double getBMI(double weight_Bmi,double height_Bmi){
		weight_Bmi = weight_Bmi * KILOGRAMS_PER_POUND ;
		height_Bmi = height_Bmi * METERS_PER_INCH ;
		double BMI = weight_Bmi /(height_Bmi*height_Bmi);
		return BMI;
	}
	
	public static String getStatus(double Bmi) {
		String Status="NaN";
		if (Bmi < 18.5) {
			Status = "Underweight";
		}
		else if (Bmi >= 18.5 && Bmi < 25.0) {
			Status = "Normal";
		}
		else if ( 25.0 <= Bmi && Bmi< 30.0 ) {
			Status = "Overweight";
		}
		else if (30.0 <= Bmi) {
			Status = "Obese";
		}
		return Status;
	}
}
