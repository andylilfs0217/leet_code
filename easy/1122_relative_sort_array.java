import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {

  public int[] relativeSortArray(int[] arr1, int[] arr2) {
    int[] ans = new int[arr1.length];
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < arr1.length; i++) {
      if (map.containsKey(arr1[i])) {
        map.put(arr1[i], map.get(arr1[i]) + 1);
      } else {
        map.put(arr1[i], 1);
      }
    }
    // Put relative order
    int curr = 0;
    for (int num : arr2) {
      for (int i = 0; i < map.get(num); i++) {
        ans[curr] = num;
        curr++;
      }
    }
    // Put remaining order
    Set<Integer> set = Arrays.stream(arr2).boxed().collect(Collectors.toSet());
    ArrayList<Integer> remainingList = new ArrayList<Integer>();
    for (int num : arr1) {
      if (!set.contains(num)) {
        remainingList.add(num);
      }
    }
    Collections.sort(remainingList);
    for (int num : remainingList) {
      ans[curr] = num;
      curr++;
    }
    return ans;
  }
}
