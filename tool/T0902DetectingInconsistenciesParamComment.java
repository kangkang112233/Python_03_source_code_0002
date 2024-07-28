package tool;
import java.io.IOException;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;

public class T0902DetectingInconsistenciesParamComment {

    private static final Pattern SPECIAL_CHAR_PATTERN = Pattern.compile("(-->|<--)");
    private static final Pattern TARGET_PATTERN = Pattern.compile("\\b[\\w_]+\\b");
    private static final Pattern TYPE_PATTERN = Pattern.compile("\\bTYPE\\b");

    private int usingChangingCount = 0;
    private int typeCount = 0;
    private Map<String, Boolean> parameterFoundInComment = new HashMap<>();
    private Set<String> actualParameterUsed = new HashSet<>();
    private boolean tempFlag = false;
    private List<String> temp = new ArrayList<>();
    private List<String> result = new ArrayList<>();

    private void checkAndOutputTodo() {
        if (usingChangingCount != typeCount) {
            temp.add("'TODO: The count of parameters and comments do not match");
        }

        List<String> sortedActualParameterUsed = new ArrayList<>(actualParameterUsed);
        List<String> sortedParameterFoundInComment = new ArrayList<>(parameterFoundInComment.keySet());

        Collections.sort(sortedActualParameterUsed);
        Collections.sort(sortedParameterFoundInComment);

        Set<String> actuallyUsedButNotInTheComment = new HashSet<>(sortedActualParameterUsed);
        actuallyUsedButNotInTheComment.removeAll(sortedParameterFoundInComment);

        Set<String> inTheCommentButNotUsed = new HashSet<>(sortedParameterFoundInComment);
        inTheCommentButNotUsed.removeAll(sortedActualParameterUsed);

        for (String expected : inTheCommentButNotUsed) {
            temp.add("'TODO: Found comment but not parameter       ## " + expected + " ## ");
        }

        for (String target : actuallyUsedButNotInTheComment) {
            temp.add("'TODO: There is no comment for this parameter__ " + target + " __ ");
        }

        result.addAll(temp);
        temp.clear();
        usingChangingCount = 0;
        typeCount = 0;
        parameterFoundInComment.clear();
        actualParameterUsed.clear();
    }

    public void processFile(String inputFile, String outputFile) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(inputFile));

        for (String line : lines) {
            Matcher specialMatcher = SPECIAL_CHAR_PATTERN.matcher(line);

            if (specialMatcher.find()) {
                usingChangingCount++;
                tempFlag = true;
                String remainingPart = line.substring(specialMatcher.end()).trim();
                Matcher match = TARGET_PATTERN.matcher(remainingPart);
                if (match.find()) {
                    parameterFoundInComment.put(match.group(), false);
                } else if (remainingPart.contains(" ")) {
                    String firstWord = remainingPart.split(" ")[0];
                    parameterFoundInComment.put(firstWord, false);
                }
            }

            if (tempFlag) {
                temp.add(line);
                if (TYPE_PATTERN.matcher(line).find()) {
                    typeCount++;
                    String[] parts = line.split("\\s+");
                    for (int i = 1; i < parts.length; i++) {
                        if (parts[i].equals("TYPE")) {
                            actualParameterUsed.add(parts[i - 1]);
                            break;
                        }
                    }
                }
                if (line.contains(".")) {
                    tempFlag = false;
                    checkAndOutputTodo();
                }
            } else {
                result.add(line);
            }
        }

        if (!temp.isEmpty()) {
            checkAndOutputTodo();
        }

        // Writing lines to output file with correct newline handling
        Path outputPath = Paths.get(outputFile);
        Files.write(outputPath, result, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
    }

    public static void main(String[] args) {
        String inputFile = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\1000_test.txt";
        String outputFile = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\2000_test.txt";

        T0902DetectingInconsistenciesParamComment processor = new T0902DetectingInconsistenciesParamComment();
        try {
            processor.processFile(inputFile, outputFile);
            System.out.println("----ok----");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
