/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    [a0,a1] = [0,1]
    for (i=0; i<n; i++) {
        [a1,a0] = [a1+a0,a1]
    }
    return a1
};

// Runtime 96 ms / Memory 42.1 MB
// debug: https://jsfiddle.net/