import java.util.Scanner;
import java.util.Arrays;
public class Q1 {

	public static void main(String[] args) {
		Scanner myScanner = new Scanner(System.in);
		Boolean[] boolArray = new Boolean[10];
		Arrays.fill(boolArray, Boolean.FALSE);
		while (true){
			
			boolean setflag = isPlaneFull(boolArray);
			if(setflag ==true) {System.out.println("the plane is now full");}
			
			System.out.println("Please type 1 for Buying First Class Ticket Please type 2 for Buying Economy Class Ticket Please type 3 for Ticket Validation \r\n"
					+ "choice: ");
			String inputString = myScanner.nextLine();
			if(inputString.equals("1")) {
				for (int i = 0; i < 10; i++) {
					if(boolArray[i]== false && i<5) {
						boolArray[i]=true;
						System.out.println("First Class Ticket is bought. Seat #"+(i+1) );
						break;
					}
						if(i>4) {
							System.out.println("First Class is full, Do you prefer Economy Class? 1. Yes, 2. No."+"choice:");
							String input = myScanner.nextLine();
							if(input.equals("1")) {
								for (int a = 5; a < 10; a++) {
									if(boolArray[a]== false) {
										boolArray[a]=true;
										System.out.println("Eco Class Ticket is bought. Seat #" + (a+1));
										break;}}}
							if(input.equals("2")) {break;}
							break;
						}
						}
					}
						
			else if(inputString.equals("2")) {
				for (int i = 5; i <= 10; i++) {
					if(i<10){
					if(boolArray[i]== false) {
						boolArray[i]=true;
						System.out.println("Eco Class Ticket is bought. Seat #"+(i+1) );
						break;
					}
				}
					if(i==10) {
							System.out.println("Eco Class is full, Do you prefer First Class? 1. Yes, 2. No."+"choice:");
							String input = myScanner.nextLine();
							if(input.equals("1")) {
								for (int a = 0; a < 10; a++) {
									if(boolArray[a]== false) {
										boolArray[a]=true;
										System.out.println("First Class Ticket is bought. Seat #" + (a+1));
										break;}}}
							if(input.equals("2")) {break;}
							break;
						
						}
				}}
			
		else if(inputString.equals("3")) {
				String seatIDString = myScanner.nextLine();
				int seatId = Integer.parseInt(seatIDString);
				validateTicketBySeatID(seatId,boolArray);
				continue;
				}

				}
	}
	
public static void validateTicketBySeatID(int seatID,Boolean[] boolArray) {
	System.out.println("Enter seat ID which will be validated" );
	if (boolArray[seatID]== true) {
		System.out.println("Ticket is sold" );
	}
	else if (boolArray[seatID]== false) {
		System.out.println("There is no seat with this id" );
	}
  }


public static boolean isPlaneFull(Boolean[] boolArray) {
	for (int i = 0; i <10; i++) {
		if (boolArray[i]== false) {
		return false;
		};
		};
		return true;
  }


}
