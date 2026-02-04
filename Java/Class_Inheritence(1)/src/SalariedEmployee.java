
public class SalariedEmployee extends Employee {
	private double weeklySalary;
	
	public SalariedEmployee(String firstName,String lastName, String socialSecurityNumber,double weeklySalary) 
	{
		super(firstName,lastName,socialSecurityNumber);
	if (weeklySalary>0) {this.weeklySalary=weeklySalary;}
	else {System.out.println("The double variable weeklySalary's input is impossible");
	System.exit(0);}}
	
	public void setWeeklySalary(double weeklySalary) {this.weeklySalary = weeklySalary;}
	
	public double getWeeklySalary() {return weeklySalary;}

	public double getPaymentAmount() {double paymentAmount= weeklySalary;return paymentAmount;}
	public String toString() {
		String string =super.toString();
		String returnString= "salaried "+string+"weekly salary: $"+weeklySalary;
		return returnString;}
}
