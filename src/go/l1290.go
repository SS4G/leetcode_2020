package main
import (
	"fmt"
)
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

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

func getDecimalValue(head *ListNode) int {
	var tmpNode *ListNode
	var intVal = 0
	var length = ListLength(head)
	for tmpNode = head; tmpNode != nil; tmpNode = tmpNode.Next {
		length--
		intVal += (1 << length) * tmpNode.Val
	}
    return intVal
}



func main() {
	var arr = []int{1,0,0,1,0,0,1,1,1,0,0,0,0,0,0}
	var head *ListNode
	var tmp *ListNode
	for idx, val := range arr {
		if idx == 0 {
			head = &ListNode{Val:val, Next:nil} 
			tmp = head
		} else {
			tmp.Next = &ListNode{Val:val, Next:nil} 
            tmp = tmp.Next
		}
	}
	fmt.Println(getDecimalValue(head))
	printList(head)
	//fmt.Println(node)
	//node.PrintNode()
}
