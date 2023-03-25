import java.util.Arrays;
import java.util.List;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        // 모음을 List로 
        List<String> moum = Arrays.asList("a", "e", "i", "o", "u");
        for (int i = 0; i < my_string.length(); i++) {
            if (!moum.contains(String.valueOf(my_string.charAt(i)))) {
                answer += my_string.charAt(i);
            }
        }
        return answer;
    }
}