/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    nums.push(target)
    nums.sort((a,b) => a-b)
    const idx = nums.findIndex(element => element == target)
    return idx
};

// Runtime 59 ms / Memory 43.5 MB
// debug: https://jsfiddle.net/