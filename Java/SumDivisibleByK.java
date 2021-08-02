import java.util.*;

class SumDivisibleByK {
	
	public int countSum(int[] a, int k) {
		int n = a.length;
		int[] freq = new int[k];

		for(int i=0; i<n; i++) {
			++freq[a[i] % k];
		}

		System.out.println(Arrays.toString(freq));

		int sum = freq[0] * (freq[0] - 1) / 2;

		System.out.println(sum);

		return 0;
	}
	public static void main(String[] args) {
		SumDivisibleByK sdk = new SumDivisibleByK();
		int[] a = { 1,3,5,7,9,4,2,8,0 };
		int k=4;
		System.out.println(sdk.countSum(a, k));
	}
}