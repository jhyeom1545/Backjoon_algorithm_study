import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine().replaceAll(" ", "");
		String asc = "12345678";
		String des = "87654321";
		if(a.equals(asc)) {
			System.out.println("ascending");
		}
		else if(a.equals(des)) {
			System.out.println("descending");
		} else {
			System.out.println("mixed");
		}
		
	}
}