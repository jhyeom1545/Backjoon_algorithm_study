
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(arr);
        // for (int i = 0; i < arr.length; i++) {
        // for (int j = i; j < arr.length; j++) {
        // if (arr[i] > arr[j]) { // 2 > 1
        // int temp = arr[j];
        // arr[j] = arr[i];
        // arr[i] = temp;
        // }
        // }
        // }
        for (int i : arr) {
            sb.append(i).append('\n');
        }
        System.out.println(sb);

    }

}
