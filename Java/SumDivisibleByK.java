import java.util.*;

class SumDivisibleByK {

	/*
		When both the remainder's of the pair are 0:

		In such a case the number of valid pairs are remf[0] * remf[0]-1.
		If there are n digits having 0 as their remainder, then the number of valid pairs are n*(n-1).

		When the sum of remainder's of the pair is equal to k:

		In such a case where the remainder's of the pair add upto make k.Then the pair is valid.

		And then we just put couple of conditions to check the hash table and find the pairs that add up and are divisible by 3.
		Like, if we get a pair whose remainders are 1 and 2 then the pair can a valid pair because they add up to become 3 which is divisible by 3.
		So Then we get an answer of 3 valid pairs for {9,4,2,8,0}
	*/
	
	public int countSum(int[] a, int k) {
		int n = a.length;
		int[] freq = new int[k];

		for(int i=0; i<n; i++) {
			++freq[a[i] % k];
		}

		System.out.println(Arrays.toString(freq));

		int sum = freq[0] * (freq[0] - 1) / 2; // n * (n-1)/2

		System.out.println(sum);

		//now we just need to count i and k-i pairs
		for(int i=1; i<=k; i++) {
			sum += freq[i] * freq[k-i]
		}

		return 0;
	}
	public static void main(String[] args) {
		SumDivisibleByK sdk = new SumDivisibleByK();
		int[] a = { 1,3,5,7,9,4,2,8,0 };
		int k=4;
		System.out.println(sdk.countSum(a, k));
	}
}