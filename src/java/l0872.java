import java.util.*;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        Set<Integer> leafs1 = getLeafValues(root1);
        Set<Integer> leafs2 = getLeafValues(root2);
        return leafs1.containsAll(leafs2) && leafs2.containsAll(leafs1);
    }

    private Set<Integer> getLeafValues(TreeNode root1) {
        if (root1 == null) {
            return new HashSet<Integer>();
        }
        else if (root1.left == null and root1.right == null) {
            return new HashSet<Integer>(){{add(root1.val)}};
        }
        else {
            Set<Integer> leftLeafValues = getLeafValues(root1.left);
            Set<Integer> rightLeafValues = getLeafValues(root1.right);
            leftLeafValues.addAll(rightLeafValues);
            return leftLeafValues;
        }
    }
}