import java.io.*;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");

		int a = Integer.parseInt(str[0]);
		int b = Integer.parseInt(str[1]);
		int c = Integer.parseInt(str[2]);
		int d = Integer.parseInt(str[3]);
		int e = Integer.parseInt(str[4]);
		
		System.out.println(((a*a)+(b*b)+(c*c)+(d*d)+(e*e))%10);
		
        br.close();
        
	}
}