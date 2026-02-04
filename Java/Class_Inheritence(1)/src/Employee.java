
public abstract class Employee implements Payable{
	private String firstName;
	private String lastName;
	private String socialSecurityNumber;

	public Employee(String firstName,String lastName, String socialSecurityNumber) 
	{this.firstName= firstName;
	this.lastName=lastName;
	this.socialSecurityNumber=socialSecurityNumber;
	}
	
	public void setFirstName (String firstName) {this.firstName =firstName; }
	public void setLastName (String lastName) {this.lastName = lastName;}
	public void setSocialSecurityNumber(String socialSecurityNumber) {this.socialSecurityNumber = socialSecurityNumber;}
	
	public String getFirstName() {return firstName;}
	public String getLastName() {return lastName;}
	public String getSocialSecurityNumber() {return socialSecurityNumber;}
	
	public String toString() {
		String returnString= "employee:  "+getFirstName()+" " +  getLastName()+ "\n"
	+"Social security number:  "+getSocialSecurityNumber()+"\n" ;
	return returnString; }
}
