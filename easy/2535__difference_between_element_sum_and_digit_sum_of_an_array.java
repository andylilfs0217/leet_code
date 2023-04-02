class Solution {

  public int differenceOfSum(int[] nums) {
    int eleSum = 0, digSum = 0;
    for (int num : nums) {
      eleSum += num;
      int numCopy = num;
      while (numCopy > 0) {
        digSum += numCopy % 10;
        numCopy /= 10;
      }
    }
    int ans = Math.abs(eleSum - digSum);
    return ans;
  }
}
