/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 package main

 type ListNode struct {
     Val int
     Next *ListNode
 }

func reverseList(head *ListNode) *ListNode {
	headNode := new(ListNode)
	headNode.Next = nil
	tmpNode := head
	var tmpNodeNext *ListNode
	for tmpNode != nil {
		tmpNodeNext = tmpNode.Next
		tmpNode.Next = headNode.Next
		headNode.Next = tmpNode
		tmpNode = tmpNodeNext
	}
	return headNode.Next
}