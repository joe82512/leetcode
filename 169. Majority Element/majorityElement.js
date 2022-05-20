/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    nums.sort()
    idx = parseInt(nums.length/2)
    return nums[idx]
};

// Runtime 72 ms / Memory 46 MB
// debug: https://jsfiddle.net/