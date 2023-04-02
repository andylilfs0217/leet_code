class Solution {

  public int countArrangement(int n) {
    Set<Integer> used = new HashSet<Integer>();
    int ans = this.helper(1, n, used);
    return ans;
  }

  private int helper(int pos, int n, Set<Integer> used) {
    int ans = 0;
    if (pos > n) {
      return 1;
    }
    for (int i = 1; i <= n; i++) {
      if (!used.contains(i) && this.checkCondition(i, pos)) {
        used.add(i);
        ans += this.helper(pos + 1, n, used);
        used.remove(i);
      }
    }
    return ans;
  }

  private boolean checkCondition(int a, int b) {
    return a % b == 0 || b % a == 0;
  }
}
