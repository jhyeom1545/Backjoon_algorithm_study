import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

       int N = Integer.parseInt(br.readLine());

       int myArr[] = new int[N];

       for(int i = 0; i < N ; i++){
         myArr[i] = Integer.parseInt(br.readLine());
       }
       for(int i = 0; i< N-1; i++){
        for(int j = 0; j < N-1-i; j++){
            if(myArr[j]>myArr[j+1]){
                int temp = myArr[j];
                myArr[j] = myArr[j+1];
                myArr[j+1] = temp;
            }
        }
       }
       for(int i = 0; i< myArr.length; i++){
        System.out.println(myArr[i]);
       }
    }
}
