package tool;
import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;

public class T08AlignUsingChangingComment {

    private static final Pattern SPECIAL_CHAR_PATTERN = Pattern.compile("(-->|<--)");
    private static final Pattern TARGET_PATTERN = Pattern.compile("\\b[\\w_]+\\b");

    public static void processFile(String inputFile, String outputFile) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(inputFile));
        List<String> temp = new ArrayList<>();
        int maxLength = 0;
        List<String> result = new ArrayList<>();

        for (String line : lines) {
            if (SPECIAL_CHAR_PATTERN.matcher(line).find()) {
                Matcher specialMatcher = SPECIAL_CHAR_PATTERN.matcher(line);
                int specialPos = 0;
                if (specialMatcher.find()) {
                    specialPos = specialMatcher.end();
                }

                if (line.length() > specialPos && line.charAt(specialPos) != ' ') {
                    temp.add(line);
                } else {
                    String remainingPart = line.substring(specialPos).trim();
                    Matcher match = TARGET_PATTERN.matcher(remainingPart);
                    if (match.find()) {
                        String firstNonEmpty = match.group(0);
                        String restOfLine = line.split(firstNonEmpty, 2)[1].trim();
                        String newLine = line.substring(0, specialPos) + firstNonEmpty + " " + restOfLine;
                        temp.add(newLine);
                    } else {
                        temp.add(line);
                    }
                }

                String[] parts = extractParts(temp.get(temp.size() - 1));
                maxLength = Math.max(maxLength, parts[1].length());
            } else {
                if (!temp.isEmpty()) {
                    processTemp(temp, maxLength, result);
                    temp.clear();
                    maxLength = 0;
                }
                result.add(line);
            }
        }

        if (!temp.isEmpty()) {
            processTemp(temp, maxLength, result);
        }

        Files.write(Paths.get(outputFile), result);
    }

    private static String[] extractParts(String line) {
        String[] parts = line.split("\\s+", 3);
        String firstPart = parts[0];
        String secondPart = parts[1];
        String thirdPart = parts.length > 2 ? parts[2].trim() : "";
        return new String[] { firstPart, secondPart, thirdPart };
    }

    private static void processTemp(List<String> temp, int maxLength, List<String> result) {
        for (String line : temp) {
            String[] parts = extractParts(line);
            String firstPart = parts[0];
            String secondPart = parts[1];
            String thirdPart = parts[2];
            int spacesNeeded = maxLength - secondPart.length();
            String formattedLine = String.format("%s    %s%s    %s", firstPart, secondPart, " ".repeat(spacesNeeded),
                    thirdPart);
            result.add(formattedLine);
        }
    }

    public static void main(String[] args) {
        String inputFile = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\1000_test.txt";
        String outputFile = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\2000_test.txt";

        try {
            processFile(inputFile, outputFile);
            System.out.println("----ok----");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
