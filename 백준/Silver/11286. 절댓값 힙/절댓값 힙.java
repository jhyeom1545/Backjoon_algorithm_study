import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> myQueue = new PriorityQueue<>((o1, o2) -> {
            // 절대값 작은 데이터 우선
            // 절댓값이 같은 경우 음수 우선
            int first_abs = Math.abs(o1);
            int second_abs = Math.abs(o2);
            if(first_abs == second_abs){
                // 1번 놈이 더 크면 양수 리턴, 아니면 음수 리턴
                return o1 > o2 ? 1 : -1;
            }
            return first_abs - second_abs;
        });
        
        for(int i = 0; i< N ; i++){
            int inputNum = Integer.parseInt(br.readLine()) ;
            if(inputNum == 0){
                if(myQueue.isEmpty()){
                    System.out.println("0");
                } else {
                    System.out.println(myQueue.poll());
                }
            } else {
                myQueue.add(inputNum);
            }
        }
    }
}