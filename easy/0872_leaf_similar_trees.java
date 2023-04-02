import java.util.ArrayList;
import javax.swing.tree.TreeNode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

  public boolean leafSimilar(TreeNode root1, TreeNode root2) {
    ArrayList<Integer> list1 = this.getLeafValueSequence(root1), list2 =
      this.getLeafValueSequence(root2);
    return list1.equals(list2);
  }

  public ArrayList<Integer> getLeafValueSequence(TreeNode root) {
    ArrayList<TreeNode> stack = new ArrayList<TreeNode>();
    stack.add(root);
    ArrayList<Integer> res = new ArrayList<Integer>();
    while (stack.size() > 0) {
      TreeNode node = stack.get(stack.size() - 1);
      stack.remove(stack.size() - 1);
      if (node.left == null && node.right == null) {
        res.add(node.val);
      } else {
        if (node.right != null) {
          stack.add(node.right);
        }
        if (node.left != null) {
          stack.add(node.left);
        }
      }
    }
    return res;
  }
}
