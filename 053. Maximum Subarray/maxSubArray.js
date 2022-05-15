/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    for (i=1;i<nums.length;i++) {
        nums[i] = Math.max(nums[i]+nums[i-1], nums[i]) // Math.max for element
    }
    return Math.max.apply(null,nums) // Math.max.apply for array
};

// Runtime 129 ms / Memory 51.1 MB
// debug: https://jsfiddle.net/