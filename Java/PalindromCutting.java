public class PalindromCutting {
	
	String cutPalindroms(String s) {
		int n = s.length();
		String newString = s;
		// System.out.println("--");
		// System.out.println("STRING "+s);

		for(int i=n; i>0 && !s.isEmpty() && s.length()>1; i--) {
			// System.out.println("I --> "+i);
			if(isPalindrom(s.substring(0, i)) && s.substring(0,i).length() > 1) {
				// System.out.println("CUTTING "+ s.substring(0, i));
				s = cutPalindroms(s.substring(i,s.length()));
			}
		}

		return s;
	}

	boolean isPalindrom(String s) {
		int i=0, j=s.length()-1;

		while(i<j) {
			if(s.charAt(i) != s.charAt(j)) return false;
			i++;
			j--;
		}
		return true;
	}

	public static void main(String[] args) {
		PalindromCutting pc = new PalindromCutting();
		System.out.println(pc.cutPalindroms("aaacodedoc"));
		System.out.println(pc.cutPalindroms("codesignal"));
		System.out.println(pc.cutPalindroms("babayaga"));
		System.out.println(pc.cutPalindroms("oobabayaga"));
		System.out.println(pc.cutPalindroms("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzatoz"));
		System.out.println(pc.cutPalindroms("abbab"));
	}
}