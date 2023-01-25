import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		int extraScore = 1;
		int result = 0;
		// 총 반복 횟수
		for (int i = 0; i < num; i++) {
			String[] str = br.readLine().split("");
			for (int j = 0; j < str.length; j++) {
				if (str[j].equals("O")) {
					result += extraScore;
					extraScore++;
				} else if (str[j].equals("X")) {
					extraScore = 1;
				}
			}
			System.out.println(result);
			result = 0;
			extraScore = 1;
		}

	}
}
