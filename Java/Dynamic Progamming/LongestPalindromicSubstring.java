class LongestPalindfromicSubstring {
    public String longestPalindrome(String s) {

        if (s.length() < 0 || s == null)
            return "";

        int start = 0, end = 0;

        for (int i = 0; i < s.length(); i++) {
            int oddLen = expandAroundCenter(i, i, s);
            int evenLen = expandAroundCenter(i, i + 1, s);

            int currentLength = end - start;

            int maxLen = Math.max(oddLen, evenLen);

            if (maxLen > currentLength) {
                start = i - (maxLen - 1) / 2;
                end = i + maxLen / 2;
            }
        }

        return s.substring(start, end + 1);
    }

    private int expandAroundCenter(int left, int right, String s) {

        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return right - left - 1;
    }
}
