import java.util.*;

public class BalancedStringCut {

    private String isValid(String s) {
        int[] letterCounts = preProcessInput(s);

        System.out.println(Arrays.toString(letterCounts));
        if (letterCounts == null)
            return "NO";

        // navigate array and check if all except one letter has the same count
        // more than 1 letter has different count return NO
        // one letter has different count but more than 1 then return NO
        // else return YES
        Arrays.sort(letterCounts);
        System.out.println(Arrays.toString(letterCounts));


        int i = 0;
        while (letterCounts[i] == 0) {
            // skip all 0 counts
            i++;
        }

        int minCount = letterCounts[i];
        int maxCount = letterCounts[letterCounts.length - 1];

        if (maxCount - minCount == 0)
            return "YES";

        // difference should be 1 and if so the count next to min should be less than
        // max count
        if (maxCount - minCount == 1 && letterCounts[letterCounts.length - 2] < maxCount)
            return "YES";

        // difference is not 1 so check if min is 1 and if so the count next to min must
        // be the same as max
        if (minCount == 1 && letterCounts[i + 1] == maxCount)
            return "YES";

        return "NO";
    }

    private static int[] preProcessInput(String s) {
        if (s == null || s.isEmpty())
            return null;
        int[] letterCounts = new int[26];
        for (char c : s.toCharArray()) {
            int index = c - 'a';
            letterCounts[index]++;
        }
        return letterCounts;
    }

    public static void main(String[] args) {
        BalancedStringCut b = new BalancedStringCut();
        String s = "dabbccd"; 
        System.out.println(b.isValid(s));

        // String s1 = "aaaab";
        // System.out.println(b.isValid(s1));
    }

   
}
