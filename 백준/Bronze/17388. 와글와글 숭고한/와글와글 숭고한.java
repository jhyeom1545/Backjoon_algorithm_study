import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		int score = 0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] array = br.readLine().split(" ");
		for (int i = 0; i < array.length; i++) {
			score += Integer.parseInt(array[i]);
			
		}
		if(score>=100) {
			System.out.println("OK");
		} else {
			int s = Integer.parseInt(array[0]); 
			int k = Integer.parseInt(array[1]);
			int h = Integer.parseInt(array[2]);
			if(s < h && s < k) {
				System.out.println("Soongsil");
			}
			if(k < s && k < h) {
				System.out.println("Korea");
			}
			if(h < s && h < k) {
				System.out.println("Hanyang");
			}
		}

	}
}