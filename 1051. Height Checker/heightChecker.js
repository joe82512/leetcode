/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    var expected = [...heights]
    expected.sort((a,b) => a-b)
    not_match = 0
    for (let i=0;i<=heights.length;i++) {
        if (expected[i]!==heights[i]) {
            not_match += 1
        }
    }
    return not_match
};

// Runtime 104 ms / Memory 42.3 MB
// debug: https://jsfiddle.net/