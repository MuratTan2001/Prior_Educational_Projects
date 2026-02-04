public class InheritanceTest {
	public static void main(String[] args) {
		BasePlusCommisionEmployee object = new BasePlusCommisionEmployee("Bob","Lewis","333-33-333",5000.00,0.04,300.00);
		double earnings = object.earnings();		
		System.out.println("Employee information obtained by get methods and earnings:\n");	
		System.out.print(object.toString());
		System.out.print("Earnings:  "+ earnings);
		System.out.println("\n\nUpdate employee information obtained by toString and earnings:\n");
		object.setBaseSalary(1000.00);
		earnings = object.earnings();
		System.out.print(object.toString());
		System.out.print("Earnings:  "+ earnings);
		}
}