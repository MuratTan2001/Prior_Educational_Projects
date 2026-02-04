
public class PayableInterfaceTest {

	public static void main(String[] args) {
		Payable payableObjects[] = new Payable[ 6 ];
		payableObjects[ 0 ] = new Invoice("01234","seat",375.00,2);
		payableObjects[ 1 ] = new Invoice("56789","tire",79.95,4);
		payableObjects[ 2 ] = new SalariedEmployee("John","Smith","111-11-1111",800.00);
		payableObjects[ 3 ] = new HourlyEmployee("Karen","Price", "222-22-2222",16.75, 40.00);
		payableObjects[ 4 ] = new CommissionEmployee("Sue","Jones","333-33-3333",10000.00,0.06);
		payableObjects[ 5 ] = new BasePlusCommissionEmployee("Bob","Lewis","444-44-4444",5000.00,0.04,300.00);
for(int i=0;i<payableObjects.length;i++) {
	System.out.println(payableObjects[i].toString());
	if ( payableObjects[i] instanceof BasePlusCommissionEmployee ) {double baseSalary=((BasePlusCommissionEmployee) payableObjects[i]).getBaseSalary();
	((BasePlusCommissionEmployee) payableObjects[i]).setBaseSalary(baseSalary*1.1);
	System.out.println("new base salary with 10% increase is: "+((BasePlusCommissionEmployee) payableObjects[i]).getBaseSalary()*(110/100));
	}
	System.out.println("payment amount: $"+payableObjects[i].getPaymentAmount()+"\n");
}
for(int j=0;j<payableObjects.length;j++) {
	System.out.println("Payable object "+j+" is a "+payableObjects[j].getClass().getName());
}
	}

}
//"payment amount: "+getPaymentAmount()+"\n"
//"new base salary with 10% increase is: "+getBaseSalary()*1.1+
//payableObjects[j].getClass().getName()