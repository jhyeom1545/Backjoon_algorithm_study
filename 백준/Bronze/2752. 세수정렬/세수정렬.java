import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int[] array = new int[3];
		array[0] = Integer.parseInt(str[0]);
		array[1] = Integer.parseInt(str[1]);
		array[2] = Integer.parseInt(str[2]);
		for (int i = 0; i < str.length - 1; i++) {
			for (int j = 0; j < str.length - 1; j++) {
				if (array[j] >= array[j + 1]) {
					int d = array[j + 1];
					array[j + 1] = array[j];
					array[j] = d;
				}
			}

		}
		int a = array[0];
		int b = array[1];
		int c = array[2];
		System.out.print(a);
		System.out.print(" " + b);
		System.out.print(" " + c);

		br.close();
	}
}