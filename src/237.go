package main 

type ListNode struct {
    Val int
    Next *ListNode
}

func (node *ListNode) PrintNode() {
	fmt.Printf("Node(%d)->", node.Val)
}

func ListLength(head *ListNode) uint {
	var tmpNode *ListNode
	var length uint = 0
	for tmpNode = head; tmpNode != nil; tmpNode = tmpNode.Next {
		length++
	}
	return length
}

func printList(head *ListNode) {
	for tmpNode := head; tmpNode != nil; tmpNode = tmpNode.Next {
        tmpNode.PrintNode()
	}
}

func deleteNode(node *ListNode) {
	node.val = node.Next.Val
	node.Next = node.Next.Next
}