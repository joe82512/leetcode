/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    const len_row = grid[0].length
    const len_column = grid.length
    var n = 0
    for (let i=0;i<len_column;i++) {
        for (let j=0;j<len_row;j++) {
            if (grid[i][j] === 1) {
                n += 4
                if ((i != 0) && (grid[i-1][j]==1)) {
                    n -= 2
                }
                if ((j != 0) && (grid[i][j-1]==1)) {
                    n -= 2
                }
            } 
        }
    }
    return n
};

// Runtime 246 ms / Memory 50.5 MB
// debug: https://jsfiddle.net/