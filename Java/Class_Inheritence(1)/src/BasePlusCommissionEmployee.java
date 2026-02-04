
public class BasePlusCommissionEmployee extends CommissionEmployee{
	private double baseSalary;
		
		public BasePlusCommissionEmployee(String firstName,String lastName, String socialSecurityNumber,double grossSales,double commissionRate,double baseSalary) 
		{
			super(firstName,lastName,socialSecurityNumber,grossSales, commissionRate);
		if (baseSalary>=0) {this.baseSalary=baseSalary;}
		else {System.out.println("The double variable baseSalary's input is impossible");
		System.exit(0);}
		}
		
		public void setBaseSalary(double baseSalary) {this.baseSalary = baseSalary;}
		public double getBaseSalary() {return baseSalary;}

		public double getPaymentAmount() {double paymentAmount= super.getPaymentAmount()+getBaseSalary();return paymentAmount;}
		public String toString() {
			String string =super.toString();
			String returnString= "base-salaried "+string+"; base salary: " +getBaseSalary();
			return returnString;}

}
