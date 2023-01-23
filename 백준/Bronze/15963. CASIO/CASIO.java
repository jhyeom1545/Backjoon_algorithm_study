import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] array = br.readLine().split(" ");
		long num1 = Long.parseLong(array[0]);
		long num2 = Long.parseLong(array[1]);
		
		if(num1 == num2) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
		
	}
}