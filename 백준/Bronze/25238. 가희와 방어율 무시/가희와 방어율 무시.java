import java.io.*;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		Long a = Long.parseLong(str[0]);
		Long b = Long.parseLong(str[1]);
		if(b==0 && a < 100) {
			System.out.println("1");
		} else if (a==0){
			System.out.println("1");
		}
		else if((a-(a*(b*0.01)))<100) {
			System.out.println("1");
		} else {
			System.out.println(0);
		}

	}
}