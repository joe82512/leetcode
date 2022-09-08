/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    let [a,b] = [0,1]
    if (n===0) {
        return a
    }
    else if (n===1) {
        return b
    }
    else {
        for (let i=0;i<n-1;i++) {
            [b,a] = [a+b,b]
        }
        return b
    }
};

// Runtime 91 ms / Memory 41.9 MB
// debug: https://jsfiddle.net/