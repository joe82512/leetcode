/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    x = matrix[0].length
    y = matrix.length
    let arr = Array.from(Array(x), () => new Array(y))
    for (var i=0;i<y;i++){
        for (var j=0;j<x;j++){
            arr[j][i] = matrix[i][j]
        }
    }
    return arr
};

// Runtime 86 ms / Memory 45.2 MB
// debug: https://jsfiddle.net/