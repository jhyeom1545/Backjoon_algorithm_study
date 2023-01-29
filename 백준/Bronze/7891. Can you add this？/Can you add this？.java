import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine()); 
		for(int i = 1; i<= num; i++) {
			String[] target = br.readLine().split(" ");
			long a = Long.parseLong(target[0]);
			long b = Long.parseLong(target[1]);
			System.out.println(a + b);
		}
		
	}
}