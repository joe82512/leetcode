/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    return n.toString(2).split('0').join('').length;
};

// Runtime 94 ms / Memory 42.4 MB
// debug: https://jsfiddle.net/