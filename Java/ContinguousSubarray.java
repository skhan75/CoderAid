import java.util.*;

class ContinguousSubarray {

	public int[] countSubarrays(int[] a) {
		Stack<Integer> stack = new Stack<>();
		int[] ans = new int[a.length];

		for(int i=0; i<a.length; i++) {
			while(!stack.isEmpty() && a[stack.peek()] < a[i])
				ans[i] += ans[stack.pop()];
			
			stack.push(i);
			ans[i]++;
		}

		stack.clear();

		int[] temp = new int[a.length];

		for(int i=a.length-1; i>=0; i--) {
			while(!stack.isEmpty() && a[stack.peek()] < a[i]) {
				int idx = stack.pop();
				ans[i] += temp[idx];
				temp[i] += temp[idx];
			}

			stack.push(i);

			temp[i]++;
		}

		return ans;
	}


	public static void main(String[] args) {
		ContinguousSubarray c = new ContinguousSubarray();
		int[] a = {3, 4, 1, 6, 2};
		System.out.println(Arrays.toString(c.countSubarrays(a)));
	}
}