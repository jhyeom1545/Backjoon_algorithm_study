import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		String stringNum = null;
		int firstNum = -1;
		int secondNum = -1;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (firstNum != 0 && secondNum != 0) {
			stringNum = br.readLine();
			StringTokenizer st = new StringTokenizer(stringNum, " ");
			firstNum = Integer.parseInt(st.nextToken());
			secondNum = Integer.parseInt(st.nextToken());
			if (firstNum == 0 && secondNum == 0) {
				break;
			}
			if (firstNum > secondNum) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}

		}

	}

}