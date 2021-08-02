public class ABBA {

	public boolean canObtain(String s, String t) {

		if(s.equals(t)) return true; 

		if(t.length() <= s.length()) return false; 
		

		if(!isSubstring(t, s) || !isSubstring(t, reverse(s))) {
			return false;
		}

		return canObtain(s+"A", t) || canObtain(reverse(s)+"B", t);

	}

	public boolean isSubstring(String t, String s) {
		return t.contains(s);
	}

	public String reverse(String word) {
		StringBuffer b = new StringBuffer();

	    for (int i = word.length() - 1; i >= 0; i--) {
	      b.append(word.charAt(i));
	    }
	    return b.toString();
	}

	public boolean canObtainOptimal(String s, String t) {

		if(s.equals(t)) return true;
		if(s.length() >= t.length()) return false;

		char last = t.charAt(t.length()-1);
		String prev; 

		if(last == 'A') {
			prev = t.substring(0, t.length()-1);
		} else {
			prev = new StringBuffer(t.substring(0, t.length()-1)).reverse().toString();
		}

		return canObtainOptimal(s, prev);

	}
	

	public static void main(String[] args) {
		ABBA abba = new ABBA();
		boolean result = abba.canObtain("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA");
		boolean result1 = abba.canObtain("B", "ABBA");
		boolean result2 = abba.canObtain("AB", "ABB");
    	System.out.println(result);
    	System.out.println(result1);
    	System.out.println(result2);

    	boolean result3 = abba.canObtainOptimal("B", "ABBA");
    	System.out.println(result3);
	}
}

// B -a-> BA -r-> ABB -a-> ABBA 
// s     	s      s        s

