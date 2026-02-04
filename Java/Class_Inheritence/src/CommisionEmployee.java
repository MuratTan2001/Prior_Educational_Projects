
public class CommisionEmployee {
	private String firstName;
	private String lastName;
	private String socialSecurityNumber;
	private double grossSales;
	private double commisionRate;
	
	public CommisionEmployee(String firstName,String lastName, String socialSecurityNumber ,double grossSales,double commisionRate ) 
	{this.firstName= firstName;
	this.lastName=lastName;
	this.socialSecurityNumber=socialSecurityNumber;
	if (grossSales>0) {this.grossSales=grossSales;}
	else {System.out.println("The double variable grossSales's input is impossible");
	System.exit(0);}
	if (commisionRate>0&&commisionRate<1) {this.commisionRate=commisionRate;}
	else {System.out.println("The double variable commisionRate's input is impossible");
	System.exit(0);}
	}
	
	public void setFirstName (String firstName) {this.firstName =firstName; }
	public void setLastName (String lastName) {this.lastName = lastName;}
	public void setSocialSecurityNumber(String socialSecurityNumber) {this.socialSecurityNumber = socialSecurityNumber;}
	public void setGrossSales(double grossSales) {
		if (grossSales>0) {this.grossSales=grossSales;}}
	public void setCommisionRate(double commisionRate) {
		if (commisionRate>0&&commisionRate<1) {this.commisionRate=commisionRate;}}
	
	public String getFirstName() {return firstName;}
	public String getLastName() {return lastName;}
	public String getSocialSecurityNumber() {return socialSecurityNumber;}
	public double getGrossSales() {return grossSales;}
	public double getCommisionRate() {return commisionRate;}
	
	public String toString() {
		String returnString= "First name:  "+getFirstName() + "\n" +"Last name:  "+  getLastName()+ "\n"
	+"Social security number:  "+getSocialSecurityNumber() + "\n" +"Gross sales:  "+ Double. toString(getGrossSales()) + "\n"
	+"Commission rate:  "+ Double.toString(getCommisionRate()) + "\n";
	return returnString; }
	public double earnings() {
		//returns the earning of employee which is calculated by multiplying grossSales and commisionRate.
		double earning = getGrossSales() * getCommisionRate();
		return earning;
	}
} 
