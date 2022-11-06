/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function(matrix) {
    [row, column] = [matrix.length, matrix[0].length]
    for (let r=0;r<row-1;r++) {
        for (let c=0;c<column-1;c++) {
            if (matrix[r][c] != matrix[r+1][c+1]) {
                return false
            }
        }
    }
    return true
};

// Runtime 108 ms / Memory 44.2 MB
// debug: https://jsfiddle.net/