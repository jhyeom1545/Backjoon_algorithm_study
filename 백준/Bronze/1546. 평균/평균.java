import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		br.readLine();
		String[] str = br.readLine().split(" ");
		double[] dbArray = new double[str.length];
		br.close();
		double result = 0;
		double resultNum = 0;
		double maxNum = 0;
		for (int i = 0; i < str.length; i++) {
			resultNum = Double.parseDouble(str[i]);
			if (resultNum > maxNum) {
				maxNum = resultNum;
			}
		}
		for (int j = 0; j < str.length; j++) {
			dbArray[j] = Double.parseDouble(str[j])/maxNum*100;
			}
		for(double num : dbArray) {
			result += num;
		}
		System.out.println(result/str.length);
	}
	
}