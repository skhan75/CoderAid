import java.util.*;

class GenerateParanthesis {
    public List<String> generateParanthesis(int n) {

        List<String> output = new ArrayList<>();
        backtrack(output, "", 0, 0, n);

        return output;
    }

    private void backtrack(List<String> output, String current, int open, int close, int max) {

        if (current.length() == max * 2) {
            output.add(current);
            return;
        }

        if (open < max)
            backtrack(output, current + "(", open + 1, close, max);

        if (close < open)
            backtrack(output, current + ")", open, close + 1, max);
    }
}
