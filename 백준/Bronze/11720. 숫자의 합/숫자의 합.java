import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String b = br.readLine();
		int result = 0;
		for (int i = 0; i < N; i++) {
			result += b.charAt(i) - 48;
		}
		System.out.println(result);
		br.close();
	}
}