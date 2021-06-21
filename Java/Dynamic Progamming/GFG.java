import java.util.*;
  
class GFG{
  
// Function to find the longest subsequence
// from the given array with maximum sum
static void longestSubWithMaxSum(int arr[], int N)
{
     
    // Stores the largest element
    // of the array
    int Max = Arrays.stream(arr).max().getAsInt();
    System.out.println("MAX "+Max);
    System.out.println("ARR "+Arrays.toString(arr));
  
    // If Max is less than 0
    if (Max < 0)
    {
         System.out.println("HERE "+Max);
        // Print the largest element
        // of the array
        System.out.print(Max);
        return;
    }
  
    // Traverse the array
    for(int i = 0; i < N; i++)
    {
         
        // If arr[i] is greater
        // than or equal to 0
        if (arr[i] >= 0)
        {
             
            // Print elements of
            // the subsequence
            System.out.print(arr[i] + " ");
        }
    }
}
  
// Driver Code
public static void main(String[] args)
{
    int arr[] = { 1, 2, -4, -2, 3, 0 };
    int N = arr.length;
  
    longestSubWithMaxSum(arr, N);
}
}