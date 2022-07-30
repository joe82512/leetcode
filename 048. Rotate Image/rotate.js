/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    matrix.reverse()
    x = matrix[0].length
    y = matrix.length  
    for (var i=0;i<y;i++){
        for (var j=i;j<x;j++){ //just get upper triangle
            [matrix[j][i], matrix[i][j]] = [matrix[i][j], matrix[j][i]] //swap
        }
    }
};

// Runtime 92 ms / Memory 42.2 MB
// debug: https://jsfiddle.net/