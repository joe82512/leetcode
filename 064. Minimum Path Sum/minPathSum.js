/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    const [row,column] = [grid.length,grid[0].length]
    for (let i=0;i<row;i++) {
        for (let j=0;j<column;j++) {
            if (i==0 & j==0) {
                grid[i][j] += 0
            }
            else if (i==0) {
                grid[i][j] += grid[i][j-1]
            }
            else if (j==0) {
                grid[i][j] += grid[i-1][j]
            }
            else {
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1])
            }
        }
    }
    return grid[row-1][column-1]
};

// Runtime 105 ms / Memory 42.8 MB
// debug: https://jsfiddle.net/