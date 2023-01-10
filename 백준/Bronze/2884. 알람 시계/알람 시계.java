import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int a = Integer.parseInt(str[0]);
		int b = Integer.parseInt(str[1]);
		// 45분 이상이면
        br.close();
		if (b < 45) {
			b = 60-(45- b);
			a = a-1;
			if(a<0) {
				a= 23;
			}
            System.out.println(a + " " + b);
		// 45분 이하면
		} else {
			System.out.println(a + " " + (b-45));
		}
	}
}
