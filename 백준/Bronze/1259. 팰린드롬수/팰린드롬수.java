import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = null;
		String b = null;
		boolean resultNO = false;
		while (true) {
			String[] arr = br.readLine().split("");
			if (Integer.parseInt(arr[0]) == 0) {
				break;
			}
			double num = Math.floor((arr.length + 1) / 2);
			double reverseNum = arr.length;
			for (double i = 0; i < num; i++) {
				a = arr[(int) i];
				b = arr[(int) (reverseNum - 1)];
				reverseNum--;
				if (!a.equals(b)) {
					System.out.println("no");
					resultNO = true;
					break;
				}
			}
			if (resultNO == false) {
				System.out.println("yes");
			} else {
				resultNO = false;
			}

		}
	}
}
