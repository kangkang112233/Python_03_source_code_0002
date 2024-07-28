package tool;
import java.util.regex.*;

public class MatcherExample {
    public static void main(String[] args) {
        String text = "Some text with --> and some more text with <-- markers.";
        Pattern pattern = Pattern.compile("(-->|<--)");
        Matcher matcher = pattern.matcher(text);

        while (matcher.find()) {
            try {
                int start = matcher.start(); // 匹配到的子字符串的起始位置
                int end = matcher.end(); // 匹配到的子字符串的结束位置
                String matched = matcher.group(); // 匹配到的子字符串

                System.out.println("Found match: " + matched);
                System.out.println("Start position: " + start);
                System.out.println("End position: " + end);
            } catch (IllegalStateException e) {
                System.err.println("Match operation is not in a valid state: " + e.getMessage());
            }
        }
    }
}
