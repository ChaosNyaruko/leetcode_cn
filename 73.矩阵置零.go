func setZeroes(matrix [][]int)  {
    firstCol0 := false
    m, n := len(matrix), len(matrix[0])
    for i := 0; i < m; i++ {
        if matrix[i][0] == 0 {
            firstCol0 =true
        }
        for j := 1; j < n; j++ {
            if matrix[i][j] == 0 {
               matrix[i][0] = 0
               matrix[0][j] = 0 
            }
        }
    }

    //fmt.Println(matrix, firstCol0)
    /*
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if matrix[i][0] == 0 || matrix[0][j] == 0 {
                matrix[i][j] = 0
            }
        }
        if firstCol0 {
            matrix[i][0] = 0
        }
    }
    for j := 1; j < n; j++ {
        if matrix[0][0] == 0 {
            matrix[0][j] = 0
        }
    }
    if firstCol0 {
        matrix[0][0] = 0
    }
    */
    for i := m - 1; i >= 0; i-- {
        for j := 1; j < n; j++ {
            if matrix[i][0] == 0 || matrix[0][j] == 0 {
                matrix[i][j] = 0
            }
        }
        if firstCol0 {
            matrix[i][0] = 0
        }
    }
}
