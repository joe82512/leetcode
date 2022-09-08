/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    let result = []
    for (let i=0; i<=n; i++) {
        let r = i.toString(2)
        result.push([...r].filter((e) => e==="1").length)
    }
    return result
};

// Runtime 204 ms / Memory 54.1 MB
// debug: https://jsfiddle.net/