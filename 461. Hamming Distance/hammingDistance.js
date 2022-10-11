/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    n = x^y;
    return n.toString(2).split('0').join('').length;
};

// Runtime 120 ms / Memory 41.7 MB
// debug: https://jsfiddle.net/