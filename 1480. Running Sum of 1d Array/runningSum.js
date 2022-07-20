/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    for (let i=1;i<nums.length;i++){
        nums[i] += nums[i-1]
    }
    return nums
};

// Runtime 81 ms / Memory 42.5 MB
// debug: https://jsfiddle.net/