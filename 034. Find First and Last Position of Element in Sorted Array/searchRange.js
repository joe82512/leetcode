/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    var result = [-1,-1]
    if (nums.includes(target)) {
        result[0] = nums.indexOf(target, 0);
        re_nums = [...nums].reverse()
        result[1] = nums.length -1 - re_nums.indexOf(target, 0);
    }
    return result
};

// Runtime 119 ms / Memory 43 MB
// debug: https://jsfiddle.net/