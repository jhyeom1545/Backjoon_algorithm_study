import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		String[] arr = br.readLine().split(" ");
		int big = Integer.parseInt(arr[0]);
		int small = Integer.parseInt(arr[0]);
		for(int i = 0; i<num;i++) {
			int compareNum = Integer.parseInt(arr[i]);
			if( compareNum > big) {
				big = compareNum;
			}
			if(compareNum < small) {
				small = compareNum;
			}
		}
		System.out.println(small+" "+big);
	}
}
