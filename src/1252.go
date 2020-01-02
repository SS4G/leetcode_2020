package main 

func oddCells(n int, m int, indices [][]int) int {	

	rowMap := make(map[int]int)
	colMap := make(map[int]int)

	for i :=0; i < len(indices); i++ {
		rowIdx := indices[i][0]
        colIdx := indices[i][1]
		if _, ok := rowMap[rowIdx]; ok {
			rowMap[rowIdx]++
		} else {
			rowMap[rowIdx] = 1
		}

		if _, ok := colMap[colIdx]; ok {
			colMap[colIdx]++
		} else {
			colMap[colIdx] = 1
		}
	}
	cnt := 0
	//fmt.Println(rowMap)
	//fmt.Println(colMap)
	for r := 0; r < n; r++ {
		for c := 0; c < m; c++ {
			rval, rok := rowMap[r]
			cval, cok := colMap[c]
			total := 0
			if rok {
				total += rval
			}
			if cok {
				total += cval
			}
			if total % 2 != 0 {
				cnt++
			}
		}
	}
	return cnt 
}

func main() {
    n := 2
    m := 3
[[0,1],[1,1]]
}