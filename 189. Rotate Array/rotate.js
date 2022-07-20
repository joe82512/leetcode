/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k % nums.length
    const s = nums.splice(-k) //splice and return delete
    nums.unshift(...s) //unshift mean add before
};

// Runtime 156 ms / Memory 50.9 MB
// debug: https://jsfiddle.net/