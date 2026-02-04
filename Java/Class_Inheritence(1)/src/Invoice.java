
public class Invoice implements Payable {
	
	private String partNumber;
	private String partDescription;
	private double pricePerItem;
	private int quantity;
	
	
	public Invoice(String partNumber,String partDescription, double pricePerItem ,int quantity) 
	{
		this.partNumber= partNumber;
		this.partDescription=partDescription;
		if (pricePerItem>0) {this.pricePerItem=pricePerItem;}
		else {System.out.println("The double variable pricePerItem's input is impossible");
		System.exit(0);}
		if (quantity>=0) {this.quantity=quantity;}
		else {System.out.println("The int variable quantity's input is impossible");
		System.exit(0);}
	}
	
	public String getPartNumber() {return this.partNumber;}
	public String getPartDescription() {return this.partDescription;}
	public double getPricePerItem() {return this.pricePerItem;}
	public int getQuantity() {return this.quantity;}
	
	public void setPartNumber(String partNumber) {this.partNumber =partNumber;}
	public void setPartDescription(String partDescription) {this.partDescription =partDescription;}
	public void setPricePerItem(double pricePerItem) {if (pricePerItem>0) {this.pricePerItem=pricePerItem;}
	else {System.out.println("The double variable pricePerItem's input is impossible");
	System.exit(0);}}
	public void setQuantity(int quantity) {if (quantity>=0) {this.quantity=quantity;}
	else {System.out.println("The int variable quantity's input is impossible");
	System.exit(0);}}
	
	public double getPaymentAmount() {double paymentAmount= getQuantity()*getPricePerItem();return paymentAmount;}
	
	public String toString(){
		String returnString = "invoice:"+"\n"+ "part number:"+this.partNumber + "(" +  this.partDescription+ ")\n"
	+"quantity: "+this.pricePerItem + "\n" +"price per item: $"+this.quantity;
	return returnString; }
	
}
