import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = { 0, 1, 0, -1 }; // 아래, 오른쪽, 위, 왼쪽 순으로 탐색
    static int[] dy = { 1, 0, -1, 0 }; //
    static boolean[][] visited;
    static int[][] A;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String line = st.nextToken(); // 110110100
            for (int j = 0; j < M; j++) {
                // 한칸한칸 잘라서 넣어 줘요
                A[i][j] = Integer.parseInt(line.substring(j, j + 1));

            }
        }
        BFS(0, 0);
        System.out.println(A[N - 1][M - 1]);
    }

    private static void BFS(int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] { i, j });
        visited[i][j] = true;
        while (!queue.isEmpty()) {
            int now[] = queue.poll();

            for (int k = 0; k < 4; k++) { // 상하 좌우 탐색
                int x = now[0] + dx[k];
                int y = now[1] + dy[k];
                if (x >= 0 && y >= 0 && x < N && y < M) { // 배열을 넘어가면 안됨
                    if (A[x][y] != 0 && !visited[x][y]) { // 0이여서 갈 수 없거나 기 방문한 것이면 안됨
                        // 갈 수 있는 곳(탐색 할 수 있는 곳)
                        visited[x][y] = true;
                        A[x][y] = A[now[0]][now[1]] + 1; // 핵심: depth를 넣어 주는곳
                        queue.add(new int[] { x, y });
                    }
                }
            }
        }

    }
}
