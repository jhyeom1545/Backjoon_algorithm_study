import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String arr = br.readLine();
		int[] resultArr = new int[26];
		
		for (int i = 0; i < arr.length(); i++) {
			int a = arr.charAt(i);
			if(arr.charAt(i)>=97 && arr.charAt(i)<=122) {
				resultArr[arr.charAt(i)-97]++;
			} else {
				resultArr[arr.charAt(i)-65]++;
			}
		}
		int max = -1;
		char ch = '?';
//		for(int a : resultArr){
//			System.out.println(a);
//		}
		for(int i = 0; i<resultArr.length;i++) {
			if(max<resultArr[i]) {
				max = resultArr[i];
				ch = (char)(i+65);
			}
			else if (resultArr[i]==max) {
				ch = '?';
			}
		}
		System.out.println(ch);
		
	}
}
