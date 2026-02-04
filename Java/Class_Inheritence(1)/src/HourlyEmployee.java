
public class HourlyEmployee extends Employee {
private double wage;
private double hours;
	
	public HourlyEmployee(String firstName,String lastName, String socialSecurityNumber,double wage,double hours) 
	{
		super(firstName,lastName,socialSecurityNumber);
	if (wage>=0) {this.wage=wage;}
	else {System.out.println("The double variable wage's input is impossible");
	System.exit(0);}
	if (hours>=0&&hours<168) {this.hours=hours;}
	else {System.out.println("The double variable hours's input is impossible");
	System.exit(0);}
	}
	
	public void setWage(double wage) {this.wage = wage;}
	public void setHours(double hours) {this.hours = hours;}
	
	public double getWage() {return wage;}
	public double getHours() {return hours;}

	public double getPaymentAmount() {double paymentAmount= wage*hours;return paymentAmount;}
	public String toString() {
		String string =super.toString();
		String returnString= "hourly "+string+"hourly wage: $"+getWage()+"; "+ "hours worked: "+getHours();
		return returnString;}
}
