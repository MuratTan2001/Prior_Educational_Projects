
public class BasePlusCommisionEmployee extends CommisionEmployee{

	private double baseSalary;
	
	public BasePlusCommisionEmployee (String firstName,String lastName, String socialSecurityNumber ,double grossSales,double commisionRate, double baseSalary) {
		super(firstName,lastName,socialSecurityNumber,grossSales,commisionRate);
	if (baseSalary>0) {this.baseSalary=baseSalary;}
	else {System.out.println("The double variable baseSalary's input is impossible");
	System.exit(0);}
	}
	public void setBaseSalary(double baseSalary) {
		if (baseSalary>0) {this.baseSalary=baseSalary;}}
	
	public double getBaseSalary() {return baseSalary;}
	
	public String toString() {
		String returnString= "First name:  "+getFirstName() + "\n" +"Last name:  "+  getLastName()+ "\n"
	+"Social security number:  "+getSocialSecurityNumber() + "\n" +"Gross sales:  "+getGrossSales() + "\n"
	+"Commission rate:  "+ getCommisionRate() + "\n" +"Base salary:  "+ getBaseSalary() +"\n";
	return returnString; }
	public double earnings() {
		//returns the earning of employee which is calculated by multiplying grossSales and commisionRate.
		double earning = getBaseSalary() + (getGrossSales() * getCommisionRate()) ;
		return earning;}
}
