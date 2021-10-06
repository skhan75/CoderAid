import java.util.*;
class FirstNonRepeatingCharacter {
	public int firstNonRepeatingCharacter(String s) {
		char[] count = new char[256];

		for(int i=0; i<s.length(); i++)
			count[s.charAt(i)]++;

		int index = -1, i;
        for (i = 0; i < s.length(); i++) {
            if (count[s.charAt(i)] == 1) {
                index = i;
                break;
            }
        }
 
        return index;
	}
	public static void main(String[] args) {
		FirstNonRepeatingCharacter fnc = new FirstNonRepeatingCharacter();
		System.out.println("First Non Repeating Character " + fnc.firstNonRepeatingCharacter("baby"));
		System.out.println("First Non Repeating Character " + fnc.firstNonRepeatingCharacter("babar"));
		System.out.println("First Non Repeating Character " + fnc.firstNonRepeatingCharacter("abcder"));
		System.out.println("First Non Repeating Character " + fnc.firstNonRepeatingCharacter("aabbccdd"));
	}
}