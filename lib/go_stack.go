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
