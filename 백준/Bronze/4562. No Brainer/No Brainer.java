import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main{
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int number = Integer.parseInt(br.readLine());
		
		for(int i = 1; i<=number; i++) {
			String str = br.readLine();
			StringTokenizer st = new StringTokenizer(str, " ");
			int firstNum = Integer.parseInt(st.nextToken());
			int secondNum = Integer.parseInt(st.nextToken());
			if(firstNum>=secondNum) {
				System.out.println("MMM BRAINS");
			} else {
				System.out.println("NO BRAINS");
			}
			
		}
	}

}