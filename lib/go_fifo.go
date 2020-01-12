package main
import "fmt"
type Fifo struct{
	array []int
	fifoCap int 
	fifoWriteIndex int 
	fifoReadIndex int
	fifoSize int
}

func (this *Fifo) FifoInit(fifoCap int) {
	this.fifoCap = fifoCap
	this.array = make([]int, this.fifoCap)
	this.fifoSize = 0
	this.fifoReadIndex = 0
	this.fifoWriteIndex = 0
}

//return error state
func (this *Fifo) FifoPush(x int) bool {
    if this.fifoCap <= this.fifoSize {
		return true
	}
	this.array[this.fifoWriteIndex] = x
	fmt.Println(this.array)
	this.fifoWriteIndex = (this.fifoWriteIndex + 1) % this.fifoCap
	this.fifoSize++
	return false
}

//return pop value and error state
func (this *Fifo) FifoPop() (int, bool) {
	if this.fifoSize <= 0 {
		return 0, true
	}
	res := this.array[this.fifoReadIndex]
	this.fifoReadIndex = (this.fifoReadIndex + 1) % this.fifoCap
	this.fifoSize--
	fmt.Println(this.array)
	return res, false
}

func (this *Fifo) FifoEmpty() bool {
	return this.fifoSize == 0
}

func (this *Fifo) FifoShow() {
	for offset := 0; offset < this.fifoSize; offset++ {
		showIdx := (this.fifoReadIndex + offset) % this.fifoCap
		fmt.Printf("%d<-", this.array[showIdx])
	}
	fmt.Printf("end fifoCap=%d fifoSize=%d\n", this.fifoCap, this.fifoSize)
}

func main() {
	var fifo *Fifo = new(Fifo)
	fifo.FifoInit(4)
	fifo.FifoPush(1)
	fifo.FifoPush(2)
	fifo.FifoPush(3)
	fifo.FifoPush(4)
	fifo.FifoPop()
	fifo.FifoPop()
	fifo.FifoPush(5)
	fifo.FifoPush(6)
	fifo.FifoShow()
}