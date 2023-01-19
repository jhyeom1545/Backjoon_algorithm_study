import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException  {
		long result = 0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			long number = Long.parseLong(br.readLine());
			if(number==-1) {
				break;
			} else {
				result += number;
			}
			
		}
		System.out.println(result);
	}}
