/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    var fc = (num) => {
        let r = 1
        for (let i=1;i<=num;i++) {
            r = r*i
        }
        return r
    }

    return fc(2*n)/(fc(n)*fc(n)*(n+1))
};

// Runtime 103 ms / Memory 42 MB
// debug: https://jsfiddle.net/