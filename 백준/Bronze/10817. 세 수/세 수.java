import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arr = br.readLine().split(" ");
        br.close();
		int num1 = Integer.parseInt(arr[0]);
		int num2 = Integer.parseInt(arr[1]);
		int num3 = Integer.parseInt(arr[2]);
		int[] intArr = { num1, num2, num3 };
		Arrays.sort(intArr);
		System.out.println(intArr[1]);
		
	}
}
