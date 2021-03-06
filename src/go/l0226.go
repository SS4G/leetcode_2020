/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main
type TreeNode struct {
	    Val int
        Left *TreeNode
        Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
		return nil
	} else {
		root.Left, root.Right = root.Right, root.Left
		invertTree(root.Right)
		invertTree(root.Left)
		return root
	}
}