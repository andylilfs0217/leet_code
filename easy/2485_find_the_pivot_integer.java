class Solution {

  public int pivotInteger(int n) {
    int l = 1, r = n;
    int ans = -1;
    while (l < r) {
      int pivot = (r + l) / 2;
      int lSum = this.getSum(1, pivot), rSum = this.getSum(pivot, n);
      if (lSum == rSum) {
        ans = pivot;
        break;
      } else if (lSum < rSum) {
        l = pivot + 1;
      } else {
        r = pivot;
      }
    }
    if (l == r) {
      int pivot = (r + l) / 2;
      int lSum = this.getSum(1, pivot), rSum = this.getSum(pivot, n);
      if (lSum == rSum) {
        ans = pivot;
      }
    }
    return ans;
  }

  public int getSum(int l, int r) {
    int ans = (l + r) * (r - l + 1) / 2;
    return ans;
  }
}
