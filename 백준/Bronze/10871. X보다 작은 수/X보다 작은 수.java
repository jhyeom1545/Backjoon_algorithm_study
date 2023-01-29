import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());
		String[] arr = br.readLine().split(" ");
		for (int i = 0; i < num1; i++) {
			if (Integer.parseInt(arr[i]) < num2) {
				System.out.print(arr[i] + " ");
			}
		}

	}
}
