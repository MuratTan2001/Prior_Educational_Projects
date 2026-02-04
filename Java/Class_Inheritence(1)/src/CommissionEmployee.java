
public class CommissionEmployee extends Employee {
private double grossSales;
private double commissionRate;
	
	public CommissionEmployee(String firstName,String lastName, String socialSecurityNumber,double grossSales,double commissionRate) 
	{
		super(firstName,lastName,socialSecurityNumber);
	if (grossSales>=0) {this.grossSales=grossSales;}
	else {System.out.println("The double variable grossSales's input is impossible");
	System.exit(0);}
	if (commissionRate>0&&commissionRate<1) {this.commissionRate=commissionRate;}
	else {System.out.println("The double variable commissionRate's input is impossible");
	System.exit(0);}
	}
	
	public void setGrossSales(double grossSales) {this.grossSales = grossSales;}
	public void setCommissionRate(double commissionRate) {this.commissionRate = commissionRate;}
	
	public double getGrossSales() {return grossSales;}
	public double getCommissionRate() {return commissionRate;}

	public double getPaymentAmount() {double paymentAmount= grossSales*commissionRate;return paymentAmount;}
	public String toString() {
		String string =super.toString();
		String returnString= "commission "+string+"gross sales: $"+getGrossSales()+"; "+ "commission rate : $"+getCommissionRate();
		return returnString;}

}
