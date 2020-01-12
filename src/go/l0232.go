package main
import (
	"fmt"
)

type Stack struct {
	stackArray []int
	topIndex int
}

func (this *Stack) StackConstructor() {
	this.stackArray = make([]int, 0, 100)
	this.topIndex = -1
	return 
}

func (this *Stack) StackPush(x int) {
	if len(this.stackArray) - 1 > this.topIndex {
		this.topIndex++
		this.stackArray[this.topIndex] = x
	} else {
		this.stackArray = append(this.stackArray, x)
		this.topIndex++
	}
}

func (this *Stack) StackPop() (int, bool) {
	if this.topIndex >= 0 {
		result := this.stackArray[this.topIndex]
		this.topIndex-- 
		return result, false
	} else {
		return 0, true
	}
}

func (this *Stack) StackPeek() (int, bool) {  
	if this.topIndex >= 0 {
		result := this.stackArray[this.topIndex]
		return result, false
	} else {
		return 0, true
	}
}

func (this *Stack) StackEmpty() bool {
	return this.topIndex == -1
}

func (this *Stack) StackSize() int {
	return this.topIndex + 1
}

func (this *Stack) StackShow() {
	fmt.Println("stack:", this.stackArray[:this.topIndex + 1])
}


type MyQueue struct {
	pushStack *Stack
	popStack *Stack 
}

func (this *MyQueue)  MyqueueInit() {
	this.pushStack = new(Stack)
	this.pushStack.StackConstructor()
	this.popStack = new(Stack)
	this.popStack.StackConstructor()
}

//trans form push to pop
func (this *MyQueue) push2Pop() {
    if this.popStack.StackSize() == 0 {
		pushSize := this.pushStack.StackSize()
		for i := 0; i < pushSize; i++ {
			popVal, _ := this.pushStack.StackPop()
			this.popStack.StackPush(popVal)
		}
	}
}


/** Initialize your data structure here. */
func Constructor() MyQueue {
	queue := new(MyQueue)
	queue.MyqueueInit()
	return *queue
}


/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int)  {
    this.pushStack.StackPush(x)
}

/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	this.push2Pop()
	if this.popStack.StackSize() > 0 {
		val, _ := this.popStack.StackPop()
		return val
	}
	return 0
}

/** Get the front element. */
func (this *MyQueue) Peek() int {
	this.push2Pop()
	if this.popStack.StackSize() > 0 {
		val, _ := this.popStack.StackPeek()
		return val
	}
    return 0
}


/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
    return this.pushStack.StackSize() == 0 && this.popStack.StackSize() == 0
}

func main() {
	// stack := new(Stack)
	// stack.stackConstructor()
	// stack.stackPush(1)
	// stack.stackPush(2)
	// stack.stackShow()
	// fmt.Println(stack.stackPop())
	// stack.stackShow()
	// fmt.Println(stack.stackEmpty())
	// stack.stackPop()
	// fmt.Println(stack.stackEmpty())
	// if val, err := stack.stackPop(); !err {
	// 	fmt.Println(val)
	// } else {
	// 	fmt.Println("error")
	// }
	obj := Constructor()
	obj.Push(1)
	obj.Push(2)
	param_3 := obj.Peek();
	param_2 := obj.Pop();
	param_4 := obj.Empty();
	fmt.Println(param_2, param_3, param_4)
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */