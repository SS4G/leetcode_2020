
import java.util.*;
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
}

class Solution {
    public int maxDepth(Node root) {
        if (root == null) {
            return 0;
        }

        List<Integer> maxDepthOfLeafs = new ArrayList<>();
        for (Node nd: root.children) {
            maxDepthOfLeafs.add(maxDepth(nd));
        }
        if (maxDepthOfLeafs.size() == 0) {
            return 1;
        }
        else {
            return Collections.max(maxDepthOfLeafs) + 1;
        }
    }
}