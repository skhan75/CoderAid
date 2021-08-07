import java.util.*;

class AlternateSort {
	
	boolean alternatingSort(int[] a) {
	    int n = a.length-1;
	    List<Integer> b = new ArrayList<>();
	    
	    if(a.length == 0) return false;
	    
	    int[] reversed = new int[a.length];
	    for (int i = 0; i <= n; i++) {
	        reversed[i] = a[n - i];
	    }
	    
	    int half = (int)Math.ceil((double)n/2);
	    int start = 0;
	    
	    int i=0, j=1;
	    while(start < half) {
	        
	        b.add(a[start]);
	        b.add(reversed[start]);
	        
	        start++;
	    }

	    
	    if(a.length%2!=0) {
	        b.add(a[start]);
	    }

	    System.out.println(b);
	    
	    if(isSorted(b)) {
	        
	        return true;
	    }
	    
	    return false;
	}

	boolean isSorted(List<Integer> list) {
	    Iterator<Integer> iter = list.iterator();
	    Integer current, previous = iter.next();
	    boolean flag = true;
	  
	    while (iter.hasNext()) {
	        current = iter.next();
	        if (previous.compareTo(current) > 0) {
	            flag =  false;
	            break;
	        }
	        previous = current;
	    }
	    
	    return flag;
	}

	public static void main(String[] args) {
		AlternateSort as = new AlternateSort();
		int[] a = {92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48};
		System.out.println(as.alternatingSort(a));
	}

	// [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48] --> FALSE



}