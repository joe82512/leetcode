/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if (matrix == []) {
        return []
    }
    else {
        const [row,column] = [matrix.length, matrix[0].length]
        var [up,down,left,right] = [0,row-1,0,column-1]
        var res = []
        while (true) {
            for (let j=left;j<=right;j++) {
                res.push(matrix[up][j])
            }                
            up += 1
            if (up > down) {break}
            
            for (let i=up;i<=down;i++) {
                res.push(matrix[i][right])
            }
            right -= 1
            if (right < left) {break}
                
            for (let j=right;j>=left;j--) {
                res.push(matrix[down][j])
            }
            down -= 1
            if (up > down) {break}

            for (let i=down;i>=up;i--) {
                res.push(matrix[i][left])
            }
            left += 1
            if (right < left) {break}
        }
        return res
    }
};

// Runtime 58 ms / Memory 41 MB
// debug: https://jsfiddle.net/