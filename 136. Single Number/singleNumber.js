/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let result = nums[0]
    for (i=1;i<nums.length;i++) {
        result ^= nums[i] // XOR
    }
    return result
};

// Runtime 89 ms / Memory 43.1 MB
// debug: https://jsfiddle.net/