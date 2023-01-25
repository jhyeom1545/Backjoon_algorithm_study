import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num1 = Integer.parseInt(br.readLine());

		// 총 반복 횟수
		for (int i = 0; i < num1; i++) {
			String[] str = br.readLine().split(" ");

			int num2 = Integer.parseInt(str[0]);
			String[] str2 = str[1].split("");

			for (int j = 0; j < str2.length; j++) {
				for (int k = 0; k < num2; k++) {
					System.out.print(str2[j]);
				}
			}
			System.out.println();
		}

	}
}