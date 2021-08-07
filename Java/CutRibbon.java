import java.util.*;
class CutRibbon{
  public static int greatestLength(int[] arr, int k) {
    int max = 0;
    for (int a : arr) {
      max = Math.max(max, a);
    }
    int lo = 1, hi = max;
    while (lo <= hi) {
      int mid = lo + (hi - lo) / 2;
      int len = getLen(arr, mid);
      if (len >= k) { lo = mid + 1; }
      else { hi = mid - 1; }
    }
    return hi;
  }
  private static int getLen(int[] arr, int target) {
    int res = 0;
    for (int a : arr) {
      res += (a / target);
    }
    return res;
  }

  public static void main(String[] args){
    int[] arr = {1, 2, 3, 4, 9};
    System.out.println(greatestLength(arr, 5));
  }
}