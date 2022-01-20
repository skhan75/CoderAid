public class ClosestPalindrome {
    
    private String nearestClosestPalindrom(String palindrome) {

        int n = palindrome.length();

        
      


        return "";
    }

    public static void main(String[] args) {
        ClosestPalindrome c = new ClosestPalindrome();
        String n = "123";
        System.out.println(c.nearestClosestPalindrom(n));
    }

    /**
     * 23|4|56
     * 23|4|32 23|5|32 ... farther away
     * 
     * Case when 10s, 1000s, 10000, ...
     * 10 --> 9 or 11
     * 1000 --> 999 or 1001
     * 
     * Case when all 9s
     * 9 --> 11
     * 99 --> 101
     * 999 --> 1001
     * 
     */
    
}
