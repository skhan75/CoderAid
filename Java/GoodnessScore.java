class GoodnessScore {

	public int goodnessScore(String s, int k) {

		int ans = 0;
		for(int i=0; i<s.length()/2; i++) {
			if(s.charAt(i) != s.charAt(s.length() - i - 1))
				ans++;
		}

		return Math.abs(ans - k);

	}

	public static void main(String[] args) {
		GoodnessScore gs = new GoodnessScore();

		String s = "CABABC";
		int k = 2;
		System.out.println("Goodness Score is "+gs.goodnessScore(s, k));

		String s1 = "ABCAA";
		int k1 = 1;
		System.out.println("Goodness Score is "+gs.goodnessScore(s1, k1));

		String s2 = "ABAA";
		int k2 = 2;
		System.out.println("Goodness Score is "+gs.goodnessScore(s2, k2));
	}
}