import java.io.*;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		ArrayList<String> list = new ArrayList<>();
		for (int i = 1; i <= a ; i++) {
			list.add(br.readLine());
		}
		for (String i : list) {
			if (i.length() >= 6 && i.length() <= 9) {
				System.out.println("yes");
			} else {
				System.out.println("no");
			}
		}
		br.close();

	}
}