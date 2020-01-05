/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
    }
		
	midIndex := len(nums) / 2
	var root *TreeNode = new(TreeNode) 
	root.Val = nums[midIndex]
	root.Left = sortedArrayToBST(nums[:midIndex])
	root.Right = sortedArrayToBST(nums[midIndex + 1:])
	return root
}