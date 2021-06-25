class GCD {

	static double gcd(double a, double b) {
		if (a == 0)
        	return b;
         
        return gcd(b%a, a);
	}
	public static void main(String[] args) {

		double a = 0, b = 0.5;
		System.out.printf("%.1f" ,gcd(a, b));

		// int a = 10, b = 15, g;
  //       g = gcd(a, b);
  //       System.out.println("GCD(" + a +  " , " + b+ ") = " + g);
         
  //       a = 35; b = 10;
  //       g = gcd(a, b);
  //       System.out.println("GCD(" + a +  " , " + b+ ") = " + g);
         
  //       a = 31; b = 2;
  //       g = gcd(a, b);
  //       System.out.println("GCD(" + a +  " , " + b+ ") = " + g);
	}
}