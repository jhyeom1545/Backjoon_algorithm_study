import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 방향이 없는 그래프가 주어졌을 때, 연결요소의 개수를 구하는 프로그램을 작성하시오
// 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다
// 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.

// 6 8 정점의 개수 간선의 개수
// 1 2
// 2 5
// 5 1
// 3 4
// 4 6
// 5 4
// 2 4
// 2 3

// 답은 1
// ----------------------------------------

// 6 5 정점의 개수 간선의 개수
// 1 2
// 2 5
// 5 1
// 3 4
// 4 6

// 답은 2

// n(노드 개수) m(에지 개수)
// A(그래프 데이터 저장 인접 리스트)
// visited(방문 기록 저장 배열)
// for(n의 개수만큼 반복하기){
//     A 인접 리스트의 각 ArrayList 초기화 하기
// }
// for(m의 개수만큼 반복하기){
//     A 인접 리스트에 그래프 데이터 저장하기
// }
// for(n의 개수만큼 반복하기){
//     if(방문하지 않은 노드가 잇으면 ){
//         연결 요소 개수++
//         DFS 실행하기
//     }
// }
// DFS 구현하기
// DFS {
//     if(현재노드 == 방문노드 return;
//     visted 배열에 현재 노드 방문 기록하기
//     현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행하기(재귀 함수 형태)
// }

public class Main {
    static boolean visited[];
    static ArrayList<Integer>[] A;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        visited = new boolean[n + 1];
        A = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) {
            A[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            // 중요 - 양쪽 방향 모두 방향성을 가지고 있기 때문에
            A[start].add(end);
            A[end].add(start);
        }
        int count = 0;
        for (int i = 1; i < n + 1; i++) {
            // 방문하지 않은 node이면
            if (!visited[i]) {
                count++;
                DFS(i);
            }
        }
        System.out.println(count);

    }

    private static void DFS(int v) {
        // 이미 방문한 노드이면 (visted==True) 종료
        if (visited[v]) {
            return;
        }
        visited[v] = true;
        for (int i : A[v]) {
            if (!visited[i]) {
                DFS(i);
            }
        }
    }
}
