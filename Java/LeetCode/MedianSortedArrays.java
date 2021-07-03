class MedianSortedArrays {
    

    public double average(int a, int b) {
        return (a+b)/2;
    }

    // Time complexity is O(log(min(m,n))
    // Space complexity is O(1)
    public double findMedianSortedArrays(int[] x, int[] y) {
    
        int m = x.length;
        int n = y.length;
        
        // Pick the smaller array as the first array
        if(m > n) {
            findMedianSortedArrays(y,x);
        }

        int elementsInPartition = (m+n+1)/2;
        int left = 0;
        int right = m; // taking right of the smaller array
       
        // We use Binary Search to find such paritions
        while(left <= right) {  

            int partitionX = (left+right)/2;
            int partitionY = (m+n+1)/2 - partitionX; // since partitionX + partitonY = m+n+1 / 2 (equal partitions)

            //if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            //if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            int maxLeftX = (partitionX==0) ? Integer.MIN_VALUE : x[partitionX-1];
            int minRightX = (partitionX==m) ? Integer.MAX_VALUE : x[partitionX]; 

            int maxLeftY = (partitionY==0) ? Integer.MIN_VALUE : y[partitionY-1];
            int minRightY = (partitionY==n) ? Integer.MAX_VALUE : y[partitionY]; 

            if(maxLeftX <= minRightY && maxLeftY <= minRightX) {
                //We have partitioned array at correct place
                // Now get max of left elements and min of right elements to get the median in case of even length combined array size
                // or get max of left for odd length combined array size.
                if((m+n)%2 == 0) {
                    return ((double) Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY))/2;
                } else { //odd
                    return ((double) Math.max(maxLeftX, maxLeftY));
                }
            } else if(maxLeftX > minRightY) { // We are far on the right side, need to move left
                right = partitionX - 1;
            } else {
                left = partitionX + 1;
            }
        }

        throw new IllegalArgumentException();
    }


    public static void main(String[] args) {
        MedianSortedArrays md = new MedianSortedArrays();

        int[] nums1 = {1,3,4,5}, nums2 = {2,6};
        System.out.println("Median of the arrays is "+ md.findMedianSortedArrays(nums1, nums2));  
    }
}