import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] array = new int[9];
		
		for(int i =0;i<9;i++) {
			array[i] = Integer.parseInt(br.readLine());
		}
		int maxNum = array[0];
		int maxlcn = 1;
		for(int j =0;j<8;j++) {
			if (maxNum<= array[j+1]) {
				maxNum = array[j+1];
				maxlcn = j+2;
			}
//			System.out.println(array[j]);
		}
		System.out.println(maxNum);
		System.out.println(maxlcn);
		
		
	br.close();
	}
}