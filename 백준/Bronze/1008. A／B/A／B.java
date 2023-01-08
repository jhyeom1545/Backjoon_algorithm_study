import java.io.*;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		Double a = Double.parseDouble(str[0]);
		Double b = Double.parseDouble(str[1]);
        br.close();
        System.out.println(a/b);
	}
}