import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
//		roomNum
		for (int i = 0; i < num; i++) {
			String[] arr = br.readLine().split(" ");
			int num1 = Integer.parseInt(arr[0]);
			int num2 = Integer.parseInt(arr[1]);
			int num3 = Integer.parseInt(arr[2]);
			if(num3 % num1==0) {
				System.out.println((num1*100)+(num3/num1));
			} else {
				System.out.println((num3%num1*100)+(num3/num1)+1);	
			}
		}
		br.close();
		
	}
}