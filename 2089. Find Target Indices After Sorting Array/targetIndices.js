/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    var result = []
    nums.sort((a,b) => a - b)
    nums.forEach((value, idx) => {
        if (value===target) {
            result.push(idx)
        }
    })
    return result
};

// Runtime 119 ms / Memory 43.7 MB
// debug: https://jsfiddle.net/