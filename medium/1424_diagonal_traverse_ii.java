class Solution {

  public int[] findDiagonalOrder(List<List<Integer>> nums) {
    List<Integer> ans = new ArrayList<Integer>();
    Set<ArrayList<Integer>> visited = new HashSet<ArrayList<Integer>>();
    visited.add(new ArrayList<Integer>(Arrays.asList(new Integer[] { 0, 0 })));
    ArrayList<int[]> queue = new ArrayList<int[]>();
    queue.add(new int[] { 0, 0 });
    while (!queue.isEmpty()) {
      ArrayList<int[]> newQueue = new ArrayList<int[]>();
      for (int[] coor : queue) {
        int x = coor[0], y = coor[1];
        ans.add(nums.get(x).get(y));
        ArrayList<Integer> temp1 = new ArrayList<Integer>(
          Arrays.asList(new Integer[] { x + 1, y })
        );
        if (
          !visited.contains(temp1) &&
          x + 1 < nums.size() &&
          y < nums.get(x + 1).size()
        ) {
          visited.add(temp1);
          newQueue.add(new int[] { x + 1, y });
        }
        ArrayList<Integer> temp2 = new ArrayList<Integer>(
          Arrays.asList(new Integer[] { x, y + 1 })
        );
        if (
          !visited.contains(temp2) &&
          x < nums.size() &&
          y + 1 < nums.get(x).size()
        ) {
          visited.add(temp2);
          newQueue.add(new int[] { x, y + 1 });
        }
      }
      queue = newQueue;
    }
    return ans.stream().mapToInt(i -> i).toArray();
  }
}
