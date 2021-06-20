 /*

 	Strong Password:
 	 - Atleast 6 characters and atmost 20 characters
 	 - Atleast one lower case, one uppercase and one digit
 	 - Doesn't contain three repeating characters in a row

	Return the number of minimum steps required to make password strong. If password is already strong return 0
 */
import java.util.Arrays;
public class StrongPasswordChecker {

 	public int check(char[] password) {

        int ops = 0;
        int missingLowerCase = 1, missingUpperCase = 1, missingDigit = 1;
        int[] temp = new int[password.length];

        for(int i=0; i<password.length; ) {
            if(Character.isLowerCase(password[i])) missingLowerCase = 0;
            if(Character.isUpperCase(password[i])) missingUpperCase = 0;
            if(Character.isDigit(password[i])) missingDigit = 0;

            int j = i;
            while(i<password.length && password[i] == password[j])  i++;
           
            temp[j] = i - j;
        }

        int total_missing = missingLowerCase + missingUpperCase + missingDigit;
 		
        // Missing characters can be added as characters to satisfy >= 6 relationship
        if(password.length < 6) {
            ops = total_missing + Math.max(0, 6 - (password.length + total_missing));
        } else {
            // Here we can use extra (over) length above 20 characters as the characters to be deleted from consecutive characters, if any
            int over_len = Math.max(password.length - 20, 0);
            int left_over = 0;

            // first we assign over length as result
            ops = over_len;

            // Then we determine the position of deleted consecutive characters
            for(int k=1; k<3; k++) { 
                //Note that if over_len is not enough, you cannot delete more
                for(int i=0; i<password.length && over_len>0; i++) {
                    if(temp[i] < 3 || temp[i]%3 != (k-1)) continue;
                    // Deleting either k characters if we have more over length characters and vice versa
                    temp[i] -= Math.min(k,over_len);
                    // Removing k characters from over length which have been used in deleting consecutive characters
                    over_len -= k;
                }
            }

            // If there are extra characters to be deleted than continue deleting them.
            for(int i=0; i<password.length; i++) {
                // System.out.println("I "+i);


                if(temp[i]>=3 && over_len>0) {
                    int need = temp[i] - 2;
                    temp[i] -= over_len;
                    over_len -= need;
                }

                //Here is the number of replacements
                //Taking aaaaa as an example, only 5/3 = 1 replacement (replace a in the middle) can eliminate consecutive characters
                if(temp[i] >= 3) left_over += temp[i] / 3;
            }

             //The number of missing characters can be used for replacement, so here is the size comparison
            ops += Math.max(total_missing, left_over);
         }


        return ops;

 		
 	}


 	public static void main(String[] args) {
 		String password = "QQQQQ";
 		StrongPasswordChecker strongPasswordChecker = new StrongPasswordChecker();
 		System.out.println("Result "+strongPasswordChecker.check(password.toCharArray()));
 	}
}